using Vortice.Direct3D11;
using Vortice.DXGI;

namespace ModMenu.Overlay.Host;

internal static class Program
{
    [STAThread]
    private static int Main(string[] args)
    {
        var pid = ParsePid(args) ?? throw new ArgumentException("--pid required");
        using var device = D3D11.D3D11CreateDevice(
            null, DriverType.Hardware, DeviceCreationFlags.BgraSupport);
        using var swap = device.QueryInterface<IDXGIDevice>().Adapter;
        Console.WriteLine($"[overlay] attached to pid={pid} d3d11 device ready");
        return new OverlayWindow(pid).Run();
    }

    private static int? ParsePid(string[] args)
    {
        for (var i = 0; i < args.Length - 1; i++)
            if (args[i] == "--pid" && int.TryParse(args[i + 1], out var p)) return p;
        return null;
    }
}