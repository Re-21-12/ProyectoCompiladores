; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"suma" = alloca i32
  store i32 0, i32* %"suma"
  %"producto" = alloca i32
  store i32 1, i32* %"producto"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"i.1" = alloca i32
  store i32 1, i32* %"i.1"
  br label %"for.cond"
for.cond:
  %"i.val" = load i32, i32* %"i.1"
  %"i.val.1" = load i32, i32* %"i.1"
  %"cmptmp" = icmp sle i32 %"i.val.1", 10
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"suma.val" = load i32, i32* %"suma"
  %"i.val.2" = load i32, i32* %"i.1"
  %"suma.val.1" = load i32, i32* %"suma"
  %"i.val.3" = load i32, i32* %"i.1"
  %"addtmp" = add i32 %"suma.val.1", %"i.val.3"
  store i32 %"addtmp", i32* %"suma"
  br label %"for.update"
for.update:
  %"i.val.4" = load i32, i32* %"i.1"
  %".10" = load i32, i32* %"i.1"
  %".11" = add i32 %".10", 1
  store i32 %".11", i32* %"i.1"
  br label %"for.cond"
for.end:
  %"j" = alloca i32
  store i32 1, i32* %"j"
  br label %"while.cond"
while.cond:
  %"j.val" = load i32, i32* %"j"
  %"j.val.1" = load i32, i32* %"j"
  %"cmptmp.1" = icmp sle i32 %"j.val.1", 5
  br i1 %"cmptmp.1", label %"while.body", label %"while.end"
while.body:
  %"producto.val" = load i32, i32* %"producto"
  %"j.val.2" = load i32, i32* %"j"
  %"producto.val.1" = load i32, i32* %"producto"
  %"j.val.3" = load i32, i32* %"j"
  %"multmp" = mul i32 %"producto.val.1", %"j.val.3"
  store i32 %"multmp", i32* %"producto"
  %"j.val.4" = load i32, i32* %"j"
  %"j.val.5" = load i32, i32* %"j"
  %"addtmp.1" = add i32 %"j.val.5", 1
  store i32 %"addtmp.1", i32* %"j"
  br label %"while.cond"
while.end:
  %"suma.val.2" = load i32, i32* %"suma"
  %".20" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i32 %"suma.val.2")
  %"producto.val.2" = load i32, i32* %"producto"
  %".22" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 %"producto.val.2")
  %"a" = alloca i32
  %"multmp.1" = mul i32 2, 3
  %"multmp.2" = mul i32 2, 3
  %"addtmp.2" = add i32 8, %"multmp.2"
  store i32 %"addtmp.2", i32* %"a"
  %"b" = alloca double
  %"divtmp" = fdiv double 0x4024000000000000, 0x4010000000000000
  store double %"divtmp", double* %"b"
  %"d" = alloca i32
  %"modtmp" = srem i32 15, 4
  store i32 %"modtmp", i32* %"d"
  %"a.val" = load i32, i32* %"a"
  %".27" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %"a.val")
  %"b.val" = load double, double* %"b"
  %".29" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", double %"b.val")
  %"d.val" = load i32, i32* %"d"
  %".31" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".32" = call i32 (i8*, ...) @"printf"(i8* %".31", i32 %"d.val")
  %"suma2" = alloca i32
  store i32 0, i32* %"suma2"
  %"producto2" = alloca i32
  store i32 1, i32* %"producto2"
  %"i2" = alloca i32
  store i32 0, i32* %"i2"
  %"i2.1" = alloca i32
  store i32 1, i32* %"i2.1"
  br label %"for.cond.1"
for.cond.1:
  %"i2.val" = load i32, i32* %"i2.1"
  %"i2.val.1" = load i32, i32* %"i2.1"
  %"cmptmp.2" = icmp sle i32 %"i2.val.1", 12
  br i1 %"cmptmp.2", label %"for.body.1", label %"for.end.1"
for.body.1:
  %"suma2.val" = load i32, i32* %"suma2"
  %"i2.val.2" = load i32, i32* %"i2.1"
  %"suma2.val.1" = load i32, i32* %"suma2"
  %"i2.val.3" = load i32, i32* %"i2.1"
  %"addtmp.3" = add i32 %"suma2.val.1", %"i2.val.3"
  store i32 %"addtmp.3", i32* %"suma2"
  br label %"for.update.1"
for.update.1:
  %"i2.val.4" = load i32, i32* %"i2.1"
  %".41" = load i32, i32* %"i2.1"
  %".42" = add i32 %".41", 1
  store i32 %".42", i32* %"i2.1"
  br label %"for.cond.1"
for.end.1:
  %"j2" = alloca i32
  store i32 1, i32* %"j2"
  br label %"while.cond.1"
while.cond.1:
  %"j2.val" = load i32, i32* %"j2"
  %"j2.val.1" = load i32, i32* %"j2"
  %"cmptmp.3" = icmp sle i32 %"j2.val.1", 6
  br i1 %"cmptmp.3", label %"while.body.1", label %"while.end.1"
while.body.1:
  %"producto2.val" = load i32, i32* %"producto2"
  %"j2.val.2" = load i32, i32* %"j2"
  %"producto2.val.1" = load i32, i32* %"producto2"
  %"j2.val.3" = load i32, i32* %"j2"
  %"multmp.3" = mul i32 %"producto2.val.1", %"j2.val.3"
  store i32 %"multmp.3", i32* %"producto2"
  %"j2.val.4" = load i32, i32* %"j2"
  %"j2.val.5" = load i32, i32* %"j2"
  %"addtmp.4" = add i32 %"j2.val.5", 1
  store i32 %"addtmp.4", i32* %"j2"
  br label %"while.cond.1"
while.end.1:
  %"suma2.val.2" = load i32, i32* %"suma2"
  %".51" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %"suma2.val.2")
  %"producto2.val.2" = load i32, i32* %"producto2"
  %".53" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".54" = call i32 (i8*, ...) @"printf"(i8* %".53", i32 %"producto2.val.2")
  %"a2" = alloca i32
  %"multmp.4" = mul i32 3, 4
  %"multmp.5" = mul i32 3, 4
  %"addtmp.5" = add i32 12, %"multmp.5"
  store i32 %"addtmp.5", i32* %"a2"
  %"b2" = alloca double
  %"divtmp.1" = fdiv double 0x4034000000000000, 0x4014000000000000
  store double %"divtmp.1", double* %"b2"
  %"d2" = alloca i32
  %"modtmp.1" = srem i32 22, 5
  store i32 %"modtmp.1", i32* %"d2"
  %"a2.val" = load i32, i32* %"a2"
  %".58" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %"a2.val")
  %"b2.val" = load double, double* %"b2"
  %".60" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".61" = call i32 (i8*, ...) @"printf"(i8* %".60", double %"b2.val")
  %"d2.val" = load i32, i32* %"d2"
  %".62" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".63" = call i32 (i8*, ...) @"printf"(i8* %".62", i32 %"d2.val")
  %"suma3" = alloca i32
  store i32 0, i32* %"suma3"
  %"producto3" = alloca i32
  store i32 1, i32* %"producto3"
  %"i3" = alloca i32
  store i32 0, i32* %"i3"
  %"i3.1" = alloca i32
  store i32 1, i32* %"i3.1"
  br label %"for.cond.2"
for.cond.2:
  %"i3.val" = load i32, i32* %"i3.1"
  %"i3.val.1" = load i32, i32* %"i3.1"
  %"cmptmp.4" = icmp sle i32 %"i3.val.1", 8
  br i1 %"cmptmp.4", label %"for.body.2", label %"for.end.2"
for.body.2:
  %"suma3.val" = load i32, i32* %"suma3"
  %"i3.val.2" = load i32, i32* %"i3.1"
  %"suma3.val.1" = load i32, i32* %"suma3"
  %"i3.val.3" = load i32, i32* %"i3.1"
  %"addtmp.6" = add i32 %"suma3.val.1", %"i3.val.3"
  store i32 %"addtmp.6", i32* %"suma3"
  br label %"for.update.2"
for.update.2:
  %"i3.val.4" = load i32, i32* %"i3.1"
  %".72" = load i32, i32* %"i3.1"
  %".73" = add i32 %".72", 1
  store i32 %".73", i32* %"i3.1"
  br label %"for.cond.2"
for.end.2:
  %"j3" = alloca i32
  store i32 1, i32* %"j3"
  br label %"while.cond.2"
while.cond.2:
  %"j3.val" = load i32, i32* %"j3"
  %"j3.val.1" = load i32, i32* %"j3"
  %"cmptmp.5" = icmp sle i32 %"j3.val.1", 4
  br i1 %"cmptmp.5", label %"while.body.2", label %"while.end.2"
while.body.2:
  %"producto3.val" = load i32, i32* %"producto3"
  %"j3.val.2" = load i32, i32* %"j3"
  %"producto3.val.1" = load i32, i32* %"producto3"
  %"j3.val.3" = load i32, i32* %"j3"
  %"multmp.6" = mul i32 %"producto3.val.1", %"j3.val.3"
  store i32 %"multmp.6", i32* %"producto3"
  %"j3.val.4" = load i32, i32* %"j3"
  %"j3.val.5" = load i32, i32* %"j3"
  %"addtmp.7" = add i32 %"j3.val.5", 1
  store i32 %"addtmp.7", i32* %"j3"
  br label %"while.cond.2"
while.end.2:
  %"suma3.val.2" = load i32, i32* %"suma3"
  %".82" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".83" = call i32 (i8*, ...) @"printf"(i8* %".82", i32 %"suma3.val.2")
  %"producto3.val.2" = load i32, i32* %"producto3"
  %".84" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".85" = call i32 (i8*, ...) @"printf"(i8* %".84", i32 %"producto3.val.2")
  %"a3" = alloca i32
  %"multmp.7" = mul i32 5, 2
  %"multmp.8" = mul i32 5, 2
  %"addtmp.8" = add i32 6, %"multmp.8"
  store i32 %"addtmp.8", i32* %"a3"
  %"b3" = alloca double
  %"divtmp.2" = fdiv double 0x402e000000000000, 0x4008000000000000
  store double %"divtmp.2", double* %"b3"
  %"d3" = alloca i32
  %"modtmp.2" = srem i32 18, 6
  store i32 %"modtmp.2", i32* %"d3"
  %"a3.val" = load i32, i32* %"a3"
  %".89" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".90" = call i32 (i8*, ...) @"printf"(i8* %".89", i32 %"a3.val")
  %"b3.val" = load double, double* %"b3"
  %".91" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".92" = call i32 (i8*, ...) @"printf"(i8* %".91", double %"b3.val")
  %"d3.val" = load i32, i32* %"d3"
  %".93" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".94" = call i32 (i8*, ...) @"printf"(i8* %".93", i32 %"d3.val")
  %"suma4" = alloca i32
  store i32 0, i32* %"suma4"
  %"producto4" = alloca i32
  store i32 1, i32* %"producto4"
  %"i4" = alloca i32
  store i32 0, i32* %"i4"
  %"i4.1" = alloca i32
  store i32 1, i32* %"i4.1"
  br label %"for.cond.3"
for.cond.3:
  %"i4.val" = load i32, i32* %"i4.1"
  %"i4.val.1" = load i32, i32* %"i4.1"
  %"cmptmp.6" = icmp sle i32 %"i4.val.1", 15
  br i1 %"cmptmp.6", label %"for.body.3", label %"for.end.3"
for.body.3:
  %"suma4.val" = load i32, i32* %"suma4"
  %"i4.val.2" = load i32, i32* %"i4.1"
  %"suma4.val.1" = load i32, i32* %"suma4"
  %"i4.val.3" = load i32, i32* %"i4.1"
  %"addtmp.9" = add i32 %"suma4.val.1", %"i4.val.3"
  store i32 %"addtmp.9", i32* %"suma4"
  br label %"for.update.3"
for.update.3:
  %"i4.val.4" = load i32, i32* %"i4.1"
  %".103" = load i32, i32* %"i4.1"
  %".104" = add i32 %".103", 1
  store i32 %".104", i32* %"i4.1"
  br label %"for.cond.3"
for.end.3:
  %"j4" = alloca i32
  store i32 1, i32* %"j4"
  br label %"while.cond.3"
while.cond.3:
  %"j4.val" = load i32, i32* %"j4"
  %"j4.val.1" = load i32, i32* %"j4"
  %"cmptmp.7" = icmp sle i32 %"j4.val.1", 7
  br i1 %"cmptmp.7", label %"while.body.3", label %"while.end.3"
while.body.3:
  %"producto4.val" = load i32, i32* %"producto4"
  %"j4.val.2" = load i32, i32* %"j4"
  %"producto4.val.1" = load i32, i32* %"producto4"
  %"j4.val.3" = load i32, i32* %"j4"
  %"multmp.9" = mul i32 %"producto4.val.1", %"j4.val.3"
  store i32 %"multmp.9", i32* %"producto4"
  %"j4.val.4" = load i32, i32* %"j4"
  %"j4.val.5" = load i32, i32* %"j4"
  %"addtmp.10" = add i32 %"j4.val.5", 1
  store i32 %"addtmp.10", i32* %"j4"
  br label %"while.cond.3"
while.end.3:
  %"suma4.val.2" = load i32, i32* %"suma4"
  %".113" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".114" = call i32 (i8*, ...) @"printf"(i8* %".113", i32 %"suma4.val.2")
  %"producto4.val.2" = load i32, i32* %"producto4"
  %".115" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".116" = call i32 (i8*, ...) @"printf"(i8* %".115", i32 %"producto4.val.2")
  %"a4" = alloca i32
  %"multmp.10" = mul i32 4, 5
  %"multmp.11" = mul i32 4, 5
  %"addtmp.11" = add i32 10, %"multmp.11"
  store i32 %"addtmp.11", i32* %"a4"
  %"b4" = alloca double
  %"divtmp.3" = fdiv double 0x4039000000000000, 0x4000000000000000
  store double %"divtmp.3", double* %"b4"
  %"d4" = alloca i32
  %"modtmp.3" = srem i32 27, 7
  store i32 %"modtmp.3", i32* %"d4"
  %"a4.val" = load i32, i32* %"a4"
  %".120" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".121" = call i32 (i8*, ...) @"printf"(i8* %".120", i32 %"a4.val")
  %"b4.val" = load double, double* %"b4"
  %".122" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".123" = call i32 (i8*, ...) @"printf"(i8* %".122", double %"b4.val")
  %"d4.val" = load i32, i32* %"d4"
  %".124" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".125" = call i32 (i8*, ...) @"printf"(i8* %".124", i32 %"d4.val")
  %"suma5" = alloca i32
  store i32 0, i32* %"suma5"
  %"producto5" = alloca i32
  store i32 1, i32* %"producto5"
  %"i5" = alloca i32
  store i32 0, i32* %"i5"
  %"i5.1" = alloca i32
  store i32 1, i32* %"i5.1"
  br label %"for.cond.4"
for.cond.4:
  %"i5.val" = load i32, i32* %"i5.1"
  %"i5.val.1" = load i32, i32* %"i5.1"
  %"cmptmp.8" = icmp sle i32 %"i5.val.1", 9
  br i1 %"cmptmp.8", label %"for.body.4", label %"for.end.4"
for.body.4:
  %"suma5.val" = load i32, i32* %"suma5"
  %"i5.val.2" = load i32, i32* %"i5.1"
  %"suma5.val.1" = load i32, i32* %"suma5"
  %"i5.val.3" = load i32, i32* %"i5.1"
  %"addtmp.12" = add i32 %"suma5.val.1", %"i5.val.3"
  store i32 %"addtmp.12", i32* %"suma5"
  br label %"for.update.4"
for.update.4:
  %"i5.val.4" = load i32, i32* %"i5.1"
  %".134" = load i32, i32* %"i5.1"
  %".135" = add i32 %".134", 1
  store i32 %".135", i32* %"i5.1"
  br label %"for.cond.4"
for.end.4:
  %"j5" = alloca i32
  store i32 1, i32* %"j5"
  br label %"while.cond.4"
while.cond.4:
  %"j5.val" = load i32, i32* %"j5"
  %"j5.val.1" = load i32, i32* %"j5"
  %"cmptmp.9" = icmp sle i32 %"j5.val.1", 3
  br i1 %"cmptmp.9", label %"while.body.4", label %"while.end.4"
while.body.4:
  %"producto5.val" = load i32, i32* %"producto5"
  %"j5.val.2" = load i32, i32* %"j5"
  %"producto5.val.1" = load i32, i32* %"producto5"
  %"j5.val.3" = load i32, i32* %"j5"
  %"multmp.12" = mul i32 %"producto5.val.1", %"j5.val.3"
  store i32 %"multmp.12", i32* %"producto5"
  %"j5.val.4" = load i32, i32* %"j5"
  %"j5.val.5" = load i32, i32* %"j5"
  %"addtmp.13" = add i32 %"j5.val.5", 1
  store i32 %"addtmp.13", i32* %"j5"
  br label %"while.cond.4"
while.end.4:
  %"suma5.val.2" = load i32, i32* %"suma5"
  %".144" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".145" = call i32 (i8*, ...) @"printf"(i8* %".144", i32 %"suma5.val.2")
  %"producto5.val.2" = load i32, i32* %"producto5"
  %".146" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".147" = call i32 (i8*, ...) @"printf"(i8* %".146", i32 %"producto5.val.2")
  %"a5" = alloca i32
  %"multmp.13" = mul i32 6, 2
  %"multmp.14" = mul i32 6, 2
  %"addtmp.14" = add i32 7, %"multmp.14"
  store i32 %"addtmp.14", i32* %"a5"
  %"b5" = alloca double
  %"divtmp.4" = fdiv double 0x4032000000000000, 0x4018000000000000
  store double %"divtmp.4", double* %"b5"
  %"d5" = alloca i32
  %"modtmp.4" = srem i32 21, 5
  store i32 %"modtmp.4", i32* %"d5"
  %"a5.val" = load i32, i32* %"a5"
  %".151" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".152" = call i32 (i8*, ...) @"printf"(i8* %".151", i32 %"a5.val")
  %"b5.val" = load double, double* %"b5"
  %".153" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".154" = call i32 (i8*, ...) @"printf"(i8* %".153", double %"b5.val")
  %"d5.val" = load i32, i32* %"d5"
  %".155" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".156" = call i32 (i8*, ...) @"printf"(i8* %".155", i32 %"d5.val")
  %"suma6" = alloca i32
  store i32 0, i32* %"suma6"
  %"producto6" = alloca i32
  store i32 1, i32* %"producto6"
  %"i6" = alloca i32
  store i32 0, i32* %"i6"
  %"i6.1" = alloca i32
  store i32 1, i32* %"i6.1"
  br label %"for.cond.5"
for.cond.5:
  %"i6.val" = load i32, i32* %"i6.1"
  %"i6.val.1" = load i32, i32* %"i6.1"
  %"cmptmp.10" = icmp sle i32 %"i6.val.1", 11
  br i1 %"cmptmp.10", label %"for.body.5", label %"for.end.5"
for.body.5:
  %"suma6.val" = load i32, i32* %"suma6"
  %"i6.val.2" = load i32, i32* %"i6.1"
  %"suma6.val.1" = load i32, i32* %"suma6"
  %"i6.val.3" = load i32, i32* %"i6.1"
  %"addtmp.15" = add i32 %"suma6.val.1", %"i6.val.3"
  store i32 %"addtmp.15", i32* %"suma6"
  br label %"for.update.5"
for.update.5:
  %"i6.val.4" = load i32, i32* %"i6.1"
  %".165" = load i32, i32* %"i6.1"
  %".166" = add i32 %".165", 1
  store i32 %".166", i32* %"i6.1"
  br label %"for.cond.5"
for.end.5:
  %"j6" = alloca i32
  store i32 1, i32* %"j6"
  br label %"while.cond.5"
while.cond.5:
  %"j6.val" = load i32, i32* %"j6"
  %"j6.val.1" = load i32, i32* %"j6"
  %"cmptmp.11" = icmp sle i32 %"j6.val.1", 8
  br i1 %"cmptmp.11", label %"while.body.5", label %"while.end.5"
while.body.5:
  %"producto6.val" = load i32, i32* %"producto6"
  %"j6.val.2" = load i32, i32* %"j6"
  %"producto6.val.1" = load i32, i32* %"producto6"
  %"j6.val.3" = load i32, i32* %"j6"
  %"multmp.15" = mul i32 %"producto6.val.1", %"j6.val.3"
  store i32 %"multmp.15", i32* %"producto6"
  %"j6.val.4" = load i32, i32* %"j6"
  %"j6.val.5" = load i32, i32* %"j6"
  %"addtmp.16" = add i32 %"j6.val.5", 1
  store i32 %"addtmp.16", i32* %"j6"
  br label %"while.cond.5"
while.end.5:
  %"suma6.val.2" = load i32, i32* %"suma6"
  %".175" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".176" = call i32 (i8*, ...) @"printf"(i8* %".175", i32 %"suma6.val.2")
  %"producto6.val.2" = load i32, i32* %"producto6"
  %".177" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".178" = call i32 (i8*, ...) @"printf"(i8* %".177", i32 %"producto6.val.2")
  %"a6" = alloca i32
  %"multmp.16" = mul i32 3, 5
  %"multmp.17" = mul i32 3, 5
  %"addtmp.17" = add i32 9, %"multmp.17"
  store i32 %"addtmp.17", i32* %"a6"
  %"b6" = alloca double
  %"divtmp.5" = fdiv double 0x403e000000000000, 0x4014000000000000
  store double %"divtmp.5", double* %"b6"
  %"d6" = alloca i32
  %"modtmp.5" = srem i32 24, 6
  store i32 %"modtmp.5", i32* %"d6"
  %"a6.val" = load i32, i32* %"a6"
  %".182" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".183" = call i32 (i8*, ...) @"printf"(i8* %".182", i32 %"a6.val")
  %"b6.val" = load double, double* %"b6"
  %".184" = bitcast [8 x i8]* @"fmt_1" to i8*
  %".185" = call i32 (i8*, ...) @"printf"(i8* %".184", double %"b6.val")
  %"d6.val" = load i32, i32* %"d6"
  %".186" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".187" = call i32 (i8*, ...) @"printf"(i8* %".186", i32 %"d6.val")
  %"suma7" = alloca i32
  store i32 0, i32* %"suma7"
  %"k1" = alloca i32
  store i32 0, i32* %"k1"
  br label %"for.cond.6"
for.cond.6:
  %"k1.val" = load i32, i32* %"k1"
  %"k1.val.1" = load i32, i32* %"k1"
  %"cmptmp.12" = icmp slt i32 %"k1.val.1", 10000
  br i1 %"cmptmp.12", label %"for.body.6", label %"for.end.6"
for.body.6:
  %"suma7.val" = load i32, i32* %"suma7"
  %"k1.val.2" = load i32, i32* %"k1"
  %"suma7.val.1" = load i32, i32* %"suma7"
  %"k1.val.3" = load i32, i32* %"k1"
  %"addtmp.18" = add i32 %"suma7.val.1", %"k1.val.3"
  store i32 %"addtmp.18", i32* %"suma7"
  br label %"for.update.6"
for.update.6:
  %"k1.val.4" = load i32, i32* %"k1"
  %".194" = load i32, i32* %"k1"
  %".195" = add i32 %".194", 1
  store i32 %".195", i32* %"k1"
  br label %"for.cond.6"
for.end.6:
  %"suma7.val.2" = load i32, i32* %"suma7"
  %".198" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".199" = call i32 (i8*, ...) @"printf"(i8* %".198", i32 %"suma7.val.2")
  %"suma8" = alloca i32
  store i32 0, i32* %"suma8"
  %"k2" = alloca i32
  store i32 0, i32* %"k2"
  br label %"for.cond.7"
for.cond.7:
  %"k2.val" = load i32, i32* %"k2"
  %"k2.val.1" = load i32, i32* %"k2"
  %"cmptmp.13" = icmp slt i32 %"k2.val.1", 10000
  br i1 %"cmptmp.13", label %"for.body.7", label %"for.end.7"
for.body.7:
  %"suma8.val" = load i32, i32* %"suma8"
  %"k2.val.2" = load i32, i32* %"k2"
  %"suma8.val.1" = load i32, i32* %"suma8"
  %"k2.val.3" = load i32, i32* %"k2"
  %"addtmp.19" = add i32 %"suma8.val.1", %"k2.val.3"
  store i32 %"addtmp.19", i32* %"suma8"
  br label %"for.update.7"
for.update.7:
  %"k2.val.4" = load i32, i32* %"k2"
  %".206" = load i32, i32* %"k2"
  %".207" = add i32 %".206", 1
  store i32 %".207", i32* %"k2"
  br label %"for.cond.7"
for.end.7:
  %"suma8.val.2" = load i32, i32* %"suma8"
  %".210" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".211" = call i32 (i8*, ...) @"printf"(i8* %".210", i32 %"suma8.val.2")
  %"suma9" = alloca i32
  store i32 0, i32* %"suma9"
  %"k3" = alloca i32
  store i32 0, i32* %"k3"
  br label %"for.cond.8"
for.cond.8:
  %"k3.val" = load i32, i32* %"k3"
  %"k3.val.1" = load i32, i32* %"k3"
  %"cmptmp.14" = icmp slt i32 %"k3.val.1", 10000
  br i1 %"cmptmp.14", label %"for.body.8", label %"for.end.8"
for.body.8:
  %"suma9.val" = load i32, i32* %"suma9"
  %"k3.val.2" = load i32, i32* %"k3"
  %"suma9.val.1" = load i32, i32* %"suma9"
  %"k3.val.3" = load i32, i32* %"k3"
  %"addtmp.20" = add i32 %"suma9.val.1", %"k3.val.3"
  store i32 %"addtmp.20", i32* %"suma9"
  br label %"for.update.8"
for.update.8:
  %"k3.val.4" = load i32, i32* %"k3"
  %".218" = load i32, i32* %"k3"
  %".219" = add i32 %".218", 1
  store i32 %".219", i32* %"k3"
  br label %"for.cond.8"
for.end.8:
  %"suma9.val.2" = load i32, i32* %"suma9"
  %".222" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".223" = call i32 (i8*, ...) @"printf"(i8* %".222", i32 %"suma9.val.2")
  %"suma10" = alloca i32
  store i32 0, i32* %"suma10"
  %"k4" = alloca i32
  store i32 0, i32* %"k4"
  br label %"for.cond.9"
for.cond.9:
  %"k4.val" = load i32, i32* %"k4"
  %"k4.val.1" = load i32, i32* %"k4"
  %"cmptmp.15" = icmp slt i32 %"k4.val.1", 10000
  br i1 %"cmptmp.15", label %"for.body.9", label %"for.end.9"
for.body.9:
  %"suma10.val" = load i32, i32* %"suma10"
  %"k4.val.2" = load i32, i32* %"k4"
  %"suma10.val.1" = load i32, i32* %"suma10"
  %"k4.val.3" = load i32, i32* %"k4"
  %"addtmp.21" = add i32 %"suma10.val.1", %"k4.val.3"
  store i32 %"addtmp.21", i32* %"suma10"
  br label %"for.update.9"
for.update.9:
  %"k4.val.4" = load i32, i32* %"k4"
  %".230" = load i32, i32* %"k4"
  %".231" = add i32 %".230", 1
  store i32 %".231", i32* %"k4"
  br label %"for.cond.9"
for.end.9:
  %"suma10.val.2" = load i32, i32* %"suma10"
  %".234" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".235" = call i32 (i8*, ...) @"printf"(i8* %".234", i32 %"suma10.val.2")
  %"suma11" = alloca i32
  store i32 0, i32* %"suma11"
  %"k5" = alloca i32
  store i32 0, i32* %"k5"
  br label %"for.cond.10"
for.cond.10:
  %"k5.val" = load i32, i32* %"k5"
  %"k5.val.1" = load i32, i32* %"k5"
  %"cmptmp.16" = icmp slt i32 %"k5.val.1", 10000
  br i1 %"cmptmp.16", label %"for.body.10", label %"for.end.10"
for.body.10:
  %"suma11.val" = load i32, i32* %"suma11"
  %"k5.val.2" = load i32, i32* %"k5"
  %"suma11.val.1" = load i32, i32* %"suma11"
  %"k5.val.3" = load i32, i32* %"k5"
  %"addtmp.22" = add i32 %"suma11.val.1", %"k5.val.3"
  store i32 %"addtmp.22", i32* %"suma11"
  br label %"for.update.10"
for.update.10:
  %"k5.val.4" = load i32, i32* %"k5"
  %".242" = load i32, i32* %"k5"
  %".243" = add i32 %".242", 1
  store i32 %".243", i32* %"k5"
  br label %"for.cond.10"
for.end.10:
  %"suma11.val.2" = load i32, i32* %"suma11"
  %".246" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".247" = call i32 (i8*, ...) @"printf"(i8* %".246", i32 %"suma11.val.2")
  %"suma12" = alloca i32
  store i32 0, i32* %"suma12"
  %"k6" = alloca i32
  store i32 0, i32* %"k6"
  br label %"for.cond.11"
for.cond.11:
  %"k6.val" = load i32, i32* %"k6"
  %"k6.val.1" = load i32, i32* %"k6"
  %"cmptmp.17" = icmp slt i32 %"k6.val.1", 10000
  br i1 %"cmptmp.17", label %"for.body.11", label %"for.end.11"
for.body.11:
  %"suma12.val" = load i32, i32* %"suma12"
  %"k6.val.2" = load i32, i32* %"k6"
  %"suma12.val.1" = load i32, i32* %"suma12"
  %"k6.val.3" = load i32, i32* %"k6"
  %"addtmp.23" = add i32 %"suma12.val.1", %"k6.val.3"
  store i32 %"addtmp.23", i32* %"suma12"
  br label %"for.update.11"
for.update.11:
  %"k6.val.4" = load i32, i32* %"k6"
  %".254" = load i32, i32* %"k6"
  %".255" = add i32 %".254", 1
  store i32 %".255", i32* %"k6"
  br label %"for.cond.11"
for.end.11:
  %"suma12.val.2" = load i32, i32* %"suma12"
  %".258" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".259" = call i32 (i8*, ...) @"printf"(i8* %".258", i32 %"suma12.val.2")
  %"resultadoSumaRec" = alloca i32
  %".265" = call i32 @"sumaRecursiva"(i32 100)
  store i32 %".265", i32* %"resultadoSumaRec"
  %"resultadoSumaRec.val" = load i32, i32* %"resultadoSumaRec"
  %".267" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".268" = call i32 (i8*, ...) @"printf"(i8* %".267", i32 %"resultadoSumaRec.val")
  ret i32 0
if.then:
  ret i32 0
if.else:
  %"n.val" = load i32, i32* %"n"
  %"n.val.1" = load i32, i32* %"n"
  %"n.val.2" = load i32, i32* %"n"
  %"subtmp" = sub i32 %"n.val.2", 1
  %".261" = call i32 @"sumaRecursiva"(i32 %"subtmp")
  %"n.val.3" = load i32, i32* %"n"
  %"n.val.4" = load i32, i32* %"n"
  %"n.val.5" = load i32, i32* %"n"
  %"subtmp.1" = sub i32 %"n.val.5", 1
  %".262" = call i32 @"sumaRecursiva"(i32 %"subtmp.1")
  %"addtmp.24" = add i32 %"n.val.3", %".262"
  ret i32 %"addtmp.24"
if.end:
  ret i32 0
}

@"fmt_0" = internal constant [8 x i8] c"%d\5c0a\5c00"
@"fmt_1" = internal constant [8 x i8] c"%f\5c0a\5c00"
define i32 @"sumaRecursiva"(i32 %".1")
{
entry:
  %"n" = alloca i32
  store i32 %".1", i32* %"n"
  %"n.val" = load i32, i32* %"n"
  %"n.val.1" = load i32, i32* %"n"
  %"cmptmp" = icmp eq i32 %"n.val.1", 0
  br i1 %"cmptmp", label %"if.then", label %"if.else"
}
