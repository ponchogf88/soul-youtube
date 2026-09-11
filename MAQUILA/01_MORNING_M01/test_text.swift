import Cocoa

let width = 1920
let height = 1080
let image = NSImage(size: NSSize(width: width, height: height))
image.lockFocus()

// Fondo 100% transparente
NSColor.clear.set()
NSRect(x: 0, y: 0, width: width, height: height).fill()

let paragraphStyle = NSMutableParagraphStyle()
paragraphStyle.alignment = .center

let attrs: [NSAttributedString.Key: Any] = [
    .font: NSFont(name: "Georgia", size: 44) ?? NSFont.systemFont(ofSize: 44, weight: .semibold),
    .foregroundColor: NSColor.white,
    .paragraphStyle: paragraphStyle,
    .strokeColor: NSColor.black.withAlphaComponent(0.8),
    .strokeWidth: -3.0
]

let text = "Detén un momento el paso... Respira la paz de este día."
let attrString = NSAttributedString(string: text, attributes: attrs)
let rect = NSRect(x: 100, y: 80, width: width - 200, height: 100)
attrString.draw(in: rect)

image.unlockFocus()

if let tiff = image.tiffRepresentation,
   let bitmap = NSBitmapImageRep(data: tiff),
   let pngData = bitmap.representation(using: .png, properties: [:]) {
    try? pngData.write(to: URL(fileURLWithPath: "test_sub.png"))
    print("PNG generado con exito nativo via Swift.")
}
