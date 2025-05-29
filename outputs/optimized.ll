; ModuleID = 'outputs/output.ll'
source_filename = "outputs/output.ll"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-unknown-linux-gnu"

; Function Attrs: nofree noreturn nosync nounwind memory(none)
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %call_fibonacci = tail call i32 @fibonacci(i32 0)
  unreachable
}

; Function Attrs: nofree noreturn nosync nounwind memory(none)
define noundef i32 @fibonacci(i32 %.1) local_unnamed_addr #0 {
entry:
  %subtmp = add i32 %.1, -1
  %call_fibonacci = tail call i32 @fibonacci(i32 %subtmp)
  unreachable
}

attributes #0 = { nofree noreturn nosync nounwind memory(none) }
