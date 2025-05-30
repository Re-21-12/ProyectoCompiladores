; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@str.1.0 = internal constant [18 x i8] c"Iniciando proceso\00"
@fmt.2 = internal constant [4 x i8] c"%d\0A\00"
@fmt.3 = internal constant [4 x i8] c"%f\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree noreturn nounwind
define noundef i32 @main() local_unnamed_addr #1 {
entry:
  %puts = tail call i32 @puts(ptr nonnull dereferenceable(1) @str.1.0)
  %.20 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 6)
  %.22 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 11)
  %.24 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 40)
  %.26 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double 5.000000e+00)
  %.30 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 6)
  br label %tailrecurse.i

tailrecurse.i:                                    ; preds = %tailrecurse.i, %entry
  br label %tailrecurse.i
}

; Function Attrs: nofree norecurse noreturn nosync nounwind memory(none)
define noundef i32 @fibonacci(i32 %.1) local_unnamed_addr #2 {
entry:
  br label %tailrecurse

tailrecurse:                                      ; preds = %tailrecurse, %entry
  br label %tailrecurse
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionA(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioA(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define noundef i1 @esParFuncA(i32 %.1) local_unnamed_addr #3 {
entry:
  ret i1 false
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionA2(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioA2(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: nofree noreturn nounwind
define noundef double @calcularPromedioA3(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.cond, %entry
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 0)
  br label %for.cond
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionB(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioB(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define noundef i1 @esParFuncB(i32 %.1) local_unnamed_addr #3 {
entry:
  ret i1 false
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionB2(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioB2(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: nofree noreturn nounwind
define noundef double @calcularPromedioB3(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.cond, %entry
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 0)
  br label %for.cond
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionC(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioC(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define noundef i1 @esParFuncC(i32 %.1) local_unnamed_addr #3 {
entry:
  ret i1 false
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionC2(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioC2(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: nofree noreturn nounwind
define noundef double @calcularPromedioC3(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.cond, %entry
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 0)
  br label %for.cond
}

; Function Attrs: nofree norecurse nosync nounwind memory(none)
define noundef i32 @factorial(i32 %.1) local_unnamed_addr #4 {
entry:
  %cmptmp = icmp sgt i32 %.1, 0
  br i1 %cmptmp, label %for.cond, label %for.end

for.cond:                                         ; preds = %entry, %for.cond
  br label %for.cond

for.end:                                          ; preds = %entry
  ret i32 1
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionD(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioD(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define noundef i1 @esImparFuncD(i32 %.1) local_unnamed_addr #3 {
entry:
  ret i1 false
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionD2(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioD2(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: nofree noreturn nounwind
define noundef double @calcularPromedioD3(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.cond, %entry
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 0)
  br label %for.cond
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionE(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioE(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define noundef i1 @esParFuncE(i32 %.1) local_unnamed_addr #3 {
entry:
  ret i1 false
}

; Function Attrs: nofree nounwind
define i32 @calcularMultiplicacionE2(i32 %.1, i32 %.2) local_unnamed_addr #0 {
entry:
  %multmp = mul i32 %.2, %.1
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %multmp)
  ret i32 %multmp
}

; Function Attrs: nofree nounwind
define double @calcularPromedioE2(double %.1, double %.2) local_unnamed_addr #0 {
entry:
  %divtmp = fdiv double %.1, %.2
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.3, double %divtmp)
  ret double %divtmp
}

; Function Attrs: nofree noreturn nounwind
define noundef double @calcularPromedioE3(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %for.cond

for.cond:                                         ; preds = %for.cond, %entry
  %.10 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 0)
  br label %for.cond
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @sumaRecursiva(i32 returned %.1) local_unnamed_addr #3 {
entry:
  ret i32 %.1
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind willreturn memory(none)
define i32 @productoRecursivo(i32 returned %.1, i32 %.2) local_unnamed_addr #3 {
entry:
  ret i32 %.1
}

; Function Attrs: nofree norecurse noreturn nosync nounwind memory(none)
define noundef i32 @potenciaRecursiva(i32 %.1, i32 %.2) local_unnamed_addr #2 {
entry:
  br label %tailrecurse

tailrecurse:                                      ; preds = %tailrecurse, %entry
  br label %tailrecurse
}

; Function Attrs: nofree noreturn nounwind
define noundef i32 @cuentaAtras(i32 %.1) local_unnamed_addr #1 {
entry:
  br label %tailrecurse

tailrecurse:                                      ; preds = %tailrecurse, %entry
  %.8 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 %.1)
  br label %tailrecurse
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
attributes #1 = { nofree noreturn nounwind }
attributes #2 = { nofree norecurse noreturn nosync nounwind memory(none) }
attributes #3 = { mustprogress nofree norecurse nosync nounwind willreturn memory(none) }
attributes #4 = { nofree norecurse nosync nounwind memory(none) }
