; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@fmt_0 = internal constant [8 x i8] c"%d\\0a\\00"
@fmt_1 = internal constant [8 x i8] c"%f\\0a\\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.21 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 55)
  %.23 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 120)
  %.28 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 14)
  %.30 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 2.500000e+00)
  %.32 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 3)
  %.52 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 78)
  %.54 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 720)
  %.59 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 24)
  %.61 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 4.000000e+00)
  %.63 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 2)
  %.83 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 36)
  %.85 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 24)
  %.90 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 16)
  %.92 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 5.000000e+00)
  %.94 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 0)
  %.114 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 120)
  %.116 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 5040)
  %.121 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 30)
  %.123 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 1.250000e+01)
  %.125 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 6)
  %.145 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 45)
  %.147 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 6)
  %.152 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 19)
  %.154 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 3.000000e+00)
  %.156 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 1)
  %.176 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 66)
  %.178 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 40320)
  %.183 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 24)
  %.185 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 6.000000e+00)
  %.187 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 0)
  %.207 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 91)
  %.209 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 362880)
  %.214 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 25)
  %.216 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 7.000000e+00)
  %.218 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 1)
  %.238 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 105)
  %.240 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 3628800)
  %.245 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 37)
  %.247 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 2.000000e+00)
  %.249 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 0)
  %.269 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 136)
  %.271 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 39916800)
  %.276 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 29)
  %.278 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 6.000000e+00)
  %.280 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 3)
  %.300 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 153)
  %.302 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 479001600)
  %.307 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 27)
  %.309 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_1, double 5.000000e+00)
  %.311 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 1)
  ret i32 0
}

attributes #0 = { nofree nounwind }
