; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@fmt.2 = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %.4 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt.2, i32 2)
  ret i32 0
}

attributes #0 = { nofree nounwind }
