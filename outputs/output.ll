; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 0, i32* %"x"
  %"x.1" = load i32, i32* %"x"
  %"cmptmp" = icmp slt i32 %"x.1", 0
  br i1 %"cmptmp", label %"then.0", label %"else.0"
ifcont:
  ret i32 0
then.0:
  %"fmtptr" = getelementptr [4 x i8], [4 x i8]* @"fmt.2", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr", i32 2)
  br label %"ifcont"
else.0:
  %"x.2" = load i32, i32* %"x"
  %"cmptmp.1" = icmp slt i32 1, %"x.2"
  br i1 %"cmptmp.1", label %"then.1", label %"else.1"
then.1:
  %"fmtptr.1" = getelementptr [4 x i8], [4 x i8]* @"fmt.3", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr.1", i32 3)
  br label %"ifcont"
else.1:
  %"fmtptr.2" = getelementptr [4 x i8], [4 x i8]* @"fmt.4", i32 0, i32 0
  %".9" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr.2", i32 4)
  br label %"ifcont"
}

@"fmt.2" = internal constant [4 x i8] c"%d\0a\00"
@"fmt.3" = internal constant [4 x i8] c"%d\0a\00"
@"fmt.4" = internal constant [4 x i8] c"%d\0a\00"