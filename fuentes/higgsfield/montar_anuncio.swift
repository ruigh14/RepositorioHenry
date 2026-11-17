import AVFoundation
import AppKit
import QuartzCore

// Montaje del anuncio RENOVA de 21 s: 2 clips + voz de Nacho + música + textos + tapas reales.
let W: CGFloat = 1080, H: CGFloat = 1920, TOTAL = 21.0
let dir = URL(fileURLWithPath: CommandLine.arguments[1])
let salida = URL(fileURLWithPath: CommandLine.arguments[2])
func u(_ n: String) -> URL { dir.appendingPathComponent(n) }

func color(_ hex: UInt32, _ a: CGFloat = 1) -> CGColor {
  CGColor(red: CGFloat((hex >> 16) & 0xFF) / 255, green: CGFloat((hex >> 8) & 0xFF) / 255,
          blue: CGFloat(hex & 0xFF) / 255, alpha: a)
}
let TINTA = color(0x141414), TURQ_TIT = color(0x0E9DB2), TURQ_CLARO = color(0x6FD8E6)
let PROFUNDO = color(0x075E6B), BLANCO = color(0xFFFFFF)

// Texto con palabras destacadas (las que van entre *asteriscos*).
func texto(_ s: String, size: CGFloat, base: CGColor, destacado: CGColor) -> NSAttributedString {
  let p = NSMutableParagraphStyle(); p.alignment = .center; p.lineSpacing = 2
  let out = NSMutableAttributedString()
  for (i, parte) in s.components(separatedBy: "*").enumerated() {
    out.append(NSAttributedString(string: parte, attributes: [
      .font: NSFont.systemFont(ofSize: size, weight: .black),
      .foregroundColor: NSColor(cgColor: i % 2 == 1 ? destacado : base)!,
      .paragraphStyle: p]))
  }
  return out
}

// Renderiza el texto como imagen (las capas de texto no se dibujan al exportar).
final class CapaTexto: CALayer {
  var texto = NSAttributedString()
  func render() {
    let sz = bounds.size, esc: CGFloat = 2
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(sz.width * esc), pixelsHigh: Int(sz.height * esc),
      bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
      bytesPerRow: 0, bitsPerPixel: 0)!
    rep.size = sz
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    let r = texto.boundingRect(with: sz, options: [.usesLineFragmentOrigin, .usesFontLeading])
    texto.draw(with: NSRect(x: 0, y: (sz.height - r.height) / 2, width: sz.width, height: r.height),
               options: [.usesLineFragmentOrigin, .usesFontLeading])
    NSGraphicsContext.restoreGraphicsState()
    contents = rep.cgImage
  }
}
func capaTexto(_ f: CGRect, _ s: NSAttributedString) -> CapaTexto {
  let t = CapaTexto(); t.frame = f; t.texto = s; t.render(); return t
}

// Visible entre t0 y t1, con fundido corto.
func mostrar(_ l: CALayer, _ t0: Double, _ t1: Double, pop: Bool = false) {
  l.opacity = 0
  let f = 0.15
  let a = CAKeyframeAnimation(keyPath: "opacity")
  a.values = [0, 0, 1, 1, 0, 0]
  a.keyTimes = [0, t0, t0 + f, t1 - f, t1, TOTAL].map { NSNumber(value: $0 / TOTAL) }
  a.duration = TOTAL; a.beginTime = AVCoreAnimationBeginTimeAtZero
  a.isRemovedOnCompletion = false; a.fillMode = .forwards
  l.add(a, forKey: "op")
  if pop {
    let s = CAKeyframeAnimation(keyPath: "transform.scale")
    s.values = [0.85, 0.85, 1.05, 1, 1]
    s.keyTimes = [0, t0, t0 + 0.2, t0 + 0.3, TOTAL].map { NSNumber(value: $0 / TOTAL) }
    s.duration = TOTAL; s.beginTime = AVCoreAnimationBeginTimeAtZero
    s.isRemovedOnCompletion = false; s.fillMode = .forwards
    l.add(s, forKey: "pop")
  }
}

// y = distancia desde ARRIBA (se convierte a coordenadas de abajo hacia arriba).
func frame(_ x: CGFloat, top: CGFloat, _ w: CGFloat, _ h: CGFloat) -> CGRect {
  CGRect(x: x, y: H - top - h, width: w, height: h)
}

func titular(_ s: String, top: CGFloat, alto: CGFloat, _ t0: Double, _ t1: Double) -> CALayer {
  let caja = CALayer(); caja.frame = frame(70, top: top, W - 140, alto)
  caja.backgroundColor = color(0xFFFFFF, 0.94); caja.cornerRadius = 28
  caja.shadowColor = .black; caja.shadowOpacity = 0.25; caja.shadowRadius = 18; caja.shadowOffset = .zero
  let t = capaTexto(CGRect(x: 30, y: 22, width: caja.bounds.width - 60, height: alto - 44),
                    texto(s, size: 62, base: TINTA, destacado: TURQ_TIT))
  caja.addSublayer(t); mostrar(caja, t0, t1, pop: true); return caja
}

func subtitulo(_ s: String, _ t0: Double, _ t1: Double) -> CALayer {
  let t = capaTexto(frame(60, top: 1330, W - 120, 200), texto(s, size: 58, base: BLANCO, destacado: TURQ_CLARO))
  t.shadowColor = .black; t.shadowOpacity = 0.9; t.shadowRadius = 8; t.shadowOffset = .zero
  mostrar(t, t0, t1); return t
}

func imagen(_ n: String) -> CGImage {
  NSImage(contentsOf: u(n))!.cgImage(forProposedRect: nil, context: nil, hints: nil)!
}

// Celular con la tapa real del ebook.
func celular(_ tapa: String, x: CGFloat, top: CGFloat, ancho: CGFloat, _ t0: Double, _ t1: Double) -> CALayer {
  let alto = ancho * 2.05
  let cuerpo = CALayer(); cuerpo.frame = frame(x, top: top, ancho, alto)
  cuerpo.backgroundColor = TINTA; cuerpo.cornerRadius = ancho * 0.13
  cuerpo.borderColor = color(0x3A3F44); cuerpo.borderWidth = 4
  cuerpo.shadowColor = .black; cuerpo.shadowOpacity = 0.45; cuerpo.shadowRadius = 30; cuerpo.shadowOffset = .zero
  let m: CGFloat = ancho * 0.045
  let pantalla = CALayer(); pantalla.frame = cuerpo.bounds.insetBy(dx: m, dy: m)
  pantalla.backgroundColor = color(0xF4F7F8); pantalla.cornerRadius = ancho * 0.10; pantalla.masksToBounds = true
  let img = imagen(tapa)
  let iw = pantalla.bounds.width - 24, ih = iw * CGFloat(img.height) / CGFloat(img.width)
  let t = CALayer(); t.contents = img; t.contentsGravity = .resizeAspect
  t.frame = CGRect(x: 12, y: (pantalla.bounds.height - ih) / 2, width: iw, height: ih)
  t.shadowColor = .black; t.shadowOpacity = 0.25; t.shadowRadius = 10; t.shadowOffset = .zero
  pantalla.addSublayer(t); cuerpo.addSublayer(pantalla)
  mostrar(cuerpo, t0, t1, pop: true); return cuerpo
}

func cierre(_ t0: Double) -> CALayer {
  let fondo = CALayer(); fondo.frame = CGRect(x: 0, y: 0, width: W, height: H); fondo.backgroundColor = PROFUNDO
  let logo = capaTexto(frame(0, top: 430, W, 170), texto("RENOVA", size: 150, base: BLANCO, destacado: BLANCO))
  let sub = capaTexto(frame(80, top: 610, W - 160, 160),
    texto("Entrenamiento, nutrición y hábitos para mujeres de *más de 35*", size: 50, base: BLANCO, destacado: TURQ_CLARO))
  fondo.addSublayer(logo); fondo.addSublayer(sub)
  let tapas = ["tapa_casa.jpg", "tapa_gym.jpg", "tapa_nutri.jpg"]
  let tw: CGFloat = 290, th = tw * 1521 / 1075, gap: CGFloat = 30
  let x0 = (W - (tw * 3 + gap * 2)) / 2
  for (i, n) in tapas.enumerated() {
    let l = CALayer(); l.contents = imagen(n); l.contentsGravity = .resizeAspect
    l.frame = frame(x0 + CGFloat(i) * (tw + gap), top: 830, tw, th)
    l.shadowColor = .black; l.shadowOpacity = 0.4; l.shadowRadius = 16; l.shadowOffset = .zero
    fondo.addSublayer(l)
  }
  let boton = CALayer(); boton.frame = frame(170, top: 1330, W - 340, 130)
  boton.backgroundColor = color(0x14B1C7); boton.cornerRadius = 65
  let bt = capaTexto(CGRect(x: 0, y: 25, width: boton.bounds.width, height: 80),
                     texto("HACÉ CLIC Y EMPEZÁ HOY", size: 50, base: BLANCO, destacado: BLANCO))
  boton.addSublayer(bt); fondo.addSublayer(boton)
  mostrar(fondo, t0, TOTAL + 0.2); return fondo
}

let sem = DispatchSemaphore(value: 0)
Task {
  do {
    let comp = AVMutableComposition()
    let vt = comp.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
    let clipA = AVURLAsset(url: u("clipA.mp4")), clipB = AVURLAsset(url: u("clipB.mp4"))
    let va = try await clipA.loadTracks(withMediaType: .video)[0]
    let vb = try await clipB.loadTracks(withMediaType: .video)[0]
    func r(_ a: Double, _ b: Double) -> CMTimeRange {
      CMTimeRange(start: CMTime(seconds: a, preferredTimescale: 600), end: CMTime(seconds: b, preferredTimescale: 600))
    }
    let cero = CMTime.zero
    try vt.insertTimeRange(r(0, 10), of: va, at: cero)
    try vt.insertTimeRange(r(0, 10), of: vb, at: CMTime(seconds: 10, preferredTimescale: 600))
    try vt.insertTimeRange(r(9, 10), of: vb, at: CMTime(seconds: 20, preferredTimescale: 600))

    let voz = AVURLAsset(url: u("locucion.wav")), mus = AVURLAsset(url: u("musica.mp3"))
    let at1 = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
    let vozT = try await voz.loadTracks(withMediaType: .audio)[0]
    let vozDur = CMTimeGetSeconds(try await voz.load(.duration))
    try at1.insertTimeRange(r(0, min(vozDur, TOTAL)), of: vozT, at: cero)
    let at2 = comp.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
    try at2.insertTimeRange(r(0, TOTAL), of: try await mus.loadTracks(withMediaType: .audio)[0], at: cero)
    let pm = AVMutableAudioMixInputParameters(track: at2)
    pm.setVolume(0.16, at: cero)
    pm.setVolumeRamp(fromStartVolume: 0.16, toEndVolume: 0.35, timeRange: r(20.4, 20.8))
    pm.setVolumeRamp(fromStartVolume: 0.35, toEndVolume: 0, timeRange: r(20.8, TOTAL))
    let mix = AVMutableAudioMix(); mix.inputParameters = [pm]

    let ins = AVMutableVideoCompositionInstruction(); ins.timeRange = r(0, TOTAL)
    let li = AVMutableVideoCompositionLayerInstruction(assetTrack: vt)
    let nat = try await va.load(.naturalSize)
    let esc = W / nat.width
    li.setTransform(CGAffineTransform(scaleX: esc, y: esc).concatenating(
      CGAffineTransform(translationX: 0, y: (H - nat.height * esc) / 2)), at: cero)
    ins.layerInstructions = [li]

    let padre = CALayer(), video = CALayer()
    padre.frame = CGRect(x: 0, y: 0, width: W, height: H); video.frame = padre.frame
    padre.addSublayer(video)
    // Titulares
    padre.addSublayer(titular("¿Llegás a casa *CANSADA* y sin tiempo para vos?", top: 210, alto: 230, 0.3, 4.5))
    padre.addSublayer(titular("*ENTRENAMIENTO* DE *FUERZA* DESDE CASA", top: 210, alto: 230, 6.3, 10.0))
    padre.addSublayer(titular("*ENTRENAMIENTOS* + *RECETAS* + TALLERES", top: 210, alto: 230, 10.2, 15.9))
    padre.addSublayer(titular("RECUPERÁ TU *FUERZA*. EMPEZÁ HOY.", top: 210, alto: 230, 16.2, 20.0))
    // Celular con el ebook real (escena del celular) y tapa de nutrición (cocina)
    padre.addSublayer(celular("tapa_casa.jpg", x: 560, top: 560, ancho: 380, 3.3, 6.4))
    padre.addSublayer(celular("tapa_nutri.jpg", x: 600, top: 640, ancho: 330, 11.0, 14.2))
    // Subtítulos, sincronizados con las pausas de la voz
    let subs: [(String, Double, Double)] = [
      ("¿Llegás a casa *cansada*,", 0.45, 2.2),
      ("sin energía y sintiendo", 2.2, 3.4),
      ("que no tenés tiempo para vos?", 3.4, 4.6),
      ("Con *RENOVA* podés empezar", 4.7, 6.3),
      ("a entrenar *fuerza* desde tu casa,", 6.3, 7.7),
      ("y organizar mejor tus comidas,", 7.8, 10.55),
      ("con *recetas* y talleres", 10.6, 12.9),
      ("para incorporar hábitos que puedas sostener.", 13.1, 16.1),
      ("Un método pensado para mujeres de más de 35.", 16.2, 18.3),
      ("Recuperá tu *fuerza* y empezá hoy.", 18.3, 19.3),
      ("¡Hacé clic y conocé *RENOVA*!", 19.3, 20.7),
    ]
    for (s, a, b) in subs { padre.addSublayer(subtitulo(s, a, b)) }
    padre.addSublayer(cierre(20.0))

    let vc = AVMutableVideoComposition()
    vc.renderSize = CGSize(width: W, height: H); vc.frameDuration = CMTime(value: 1, timescale: 30)
    vc.instructions = [ins]
    vc.animationTool = AVVideoCompositionCoreAnimationTool(postProcessingAsVideoLayer: video, in: padre)

    try? FileManager.default.removeItem(at: salida)
    let ex = AVAssetExportSession(asset: comp, presetName: AVAssetExportPresetHighestQuality)!
    ex.videoComposition = vc; ex.audioMix = mix
    try await ex.export(to: salida, as: .mp4)
    print("OK", salida.path)
  } catch { print("ERROR", error) }
  sem.signal()
}
sem.wait()
