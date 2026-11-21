using System.Runtime.InteropServices;

namespace ModMenu.Overlay.Host;

internal sealed class OverlayWindow
{
    private readonly int _pid;
    private bool _menuOpen;

    public OverlayWindow(int pid) => _pid = pid;

    public int Run()
    {
        while (IsProcessAlive(_pid))
        {
            if (GetAsyncKeyState(0x2D) < 0) _menuOpen = !_menuOpen;
            if (_menuOpen) DrawMenu();
            Thread.Sleep(16);
        }
        return 0;
    }

    private void DrawMenu()
    {
        // ImGui frame rendered over the game's swapchain
    }

    [DllImport("user32.dll")] private static extern short GetAsyncKeyState(int vKey);
    [DllImport("kernel32.dll")] private static extern IntPtr OpenProcess(int access, bool inherit, int pid);
    [DllImport("kernel32.dll")] private static extern bool CloseHandle(IntPtr h);

    private static bool IsProcessAlive(int pid)
    {
        var h = OpenProcess(0x1000, false, pid);
        if (h == IntPtr.Zero) return false;
        CloseHandle(h);
        return true;
    }
}