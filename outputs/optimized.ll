; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

@fmt_0 = internal constant [8 x i8] c"%d\\0a\\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  br label %for.body

for.body:                                         ; preds = %entry, %for.body
  %i.05 = phi i32 [ 0, %entry ], [ %.9, %for.body ]
  %.6 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @fmt_0, i32 %i.05)
  %.9 = add nuw nsw i32 %i.05, 1
  %exitcond.not = icmp eq i32 %.9, 100000
  br i1 %exitcond.not, label %for.end, label %for.body

for.end:                                          ; preds = %for.body
  ret i32 0
}

attributes #0 = { nofree nounwind }
