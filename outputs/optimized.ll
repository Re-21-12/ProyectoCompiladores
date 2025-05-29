; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

; Function Attrs: nofree norecurse noreturn nosync nounwind memory(none)
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  br label %tailrecurse.i

tailrecurse.i:                                    ; preds = %tailrecurse.i, %entry
  br label %tailrecurse.i
}

; Function Attrs: nofree norecurse noreturn nosync nounwind memory(none)
define noundef i32 @fibonacci(i32 %.1) local_unnamed_addr #0 {
entry:
  br label %tailrecurse

tailrecurse:                                      ; preds = %tailrecurse, %entry
  br label %tailrecurse
}

attributes #0 = { nofree norecurse noreturn nosync nounwind memory(none) }
