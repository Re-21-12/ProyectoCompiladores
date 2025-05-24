; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"contadorA" = alloca i32
  store i32 0, i32* %"contadorA"
  %"sumaA" = alloca i32
  store i32 0, i32* %"sumaA"
  %"sumaA2" = alloca i32
  store i32 0, i32* %"sumaA2"
  %"mensajeA" = alloca i8*
  %"str.1.0_ptr" = getelementptr [18 x i8], [18 x i8]* @"str.1.0", i32 0, i32 0
  store i8* %"str.1.0_ptr", i8** %"mensajeA"
  %"es_validoA" = alloca i1
  store i1 1, i1* %"es_validoA"
  %"es_adminA" = alloca i1
  store i1 0, i1* %"es_adminA"
  %"contadorA2" = alloca i32
  store i32 0, i32* %"contadorA2"
  %"sumaA3" = alloca i32
  store i32 0, i32* %"sumaA3"
  %"sumaA4" = alloca i32
  store i32 0, i32* %"sumaA4"
  %"mensajeA1" = alloca i8*
  %"mensajeA1_ptr_cast" = getelementptr [18 x i8], [18 x i8]* @"str.1.0", i32 0, i32 0
  store i8* %"mensajeA1_ptr_cast", i8** %"mensajeA1"
  %"es_validoA2" = alloca i1
  store i1 1, i1* %"es_validoA2"
  %"mensajeA.val" = load i8*, i8** %"mensajeA"
  %".13" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8* %"mensajeA.val")
  %"resultadoA1" = alloca i32
  %"addtmp" = add i32 6, 4
  store i32 %"addtmp", i32* %"resultadoA1"
  %"resultadoA2" = alloca i32
  %"subtmp" = sub i32 11, 3
  store i32 %"subtmp", i32* %"resultadoA2"
  %"resultadoA3" = alloca i32
  %"multmp" = mul i32 5, 8
  store i32 %"multmp", i32* %"resultadoA3"
  %"resultadoA4" = alloca double
  %"divtmp" = fdiv double 0x4039000000000000, 0x4014000000000000
  store double %"divtmp", double* %"resultadoA4"
  %"resultadoA1.val" = load i32, i32* %"resultadoA1"
  %".19" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %"resultadoA1.val")
  %"resultadoA2.val" = load i32, i32* %"resultadoA2"
  %".21" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %"resultadoA2.val")
  %"resultadoA3.val" = load i32, i32* %"resultadoA3"
  %".23" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %"resultadoA3.val")
  %"resultadoA4.val" = load double, double* %"resultadoA4"
  %".25" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", double %"resultadoA4.val")
  %"totalA" = alloca i32
  %"resultadoA1.val.1" = load i32, i32* %"resultadoA1"
  %"resultadoA2.val.1" = load i32, i32* %"resultadoA2"
  %"addtmp.1" = add i32 %"resultadoA1.val.1", %"resultadoA2.val.1"
  store i32 %"addtmp.1", i32* %"totalA"
  %"totalA2" = alloca i32
  %"resultadoA3.val.1" = load i32, i32* %"resultadoA3"
  %"resultadoA1.val.2" = load i32, i32* %"resultadoA1"
  %"multmp.1" = mul i32 %"resultadoA3.val.1", %"resultadoA1.val.2"
  store i32 %"multmp.1", i32* %"totalA2"
  %"totalA.val" = load i32, i32* %"totalA"
  %".29" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %"totalA.val")
  %"asd" = alloca i32
  store i32 0, i32* %"asd"
  %"limite" = alloca i32
  store i32 10, i32* %"limite"
  br label %"while.cond"
while.cond:
  %"asd.val" = load i32, i32* %"asd"
  %"limite.val" = load i32, i32* %"limite"
  %"cmptmp" = icmp slt i32 %"asd.val", %"limite.val"
  br i1 %"cmptmp", label %"while.body", label %"while.end"
while.body:
  %"asd.val.1" = load i32, i32* %"asd"
  %"call_fibonacci" = call i32 @"fibonacci"(i32 %"asd.val.1")
  %".35" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", i32 %"call_fibonacci")
  br label %"while.cond"
while.end:
  %".38" = icmp ne i32 0, 0
  br i1 %".38", label %"if.then", label %"if.end"
if.then:
  br label %"if.end"
if.end:
  %"j" = alloca i32
  store i32 0, i32* %"j"
  br label %"for.cond"
for.cond:
  %"j.val" = load i32, i32* %"j"
  %"cmptmp.1" = icmp slt i32 %"j.val", 10000
  br i1 %"cmptmp.1", label %"for.body", label %"for.end"
for.body:
  %"sumaA.val" = load i32, i32* %"sumaA"
  %"j.val.1" = load i32, i32* %"j"
  %"addtmp.2" = add i32 %"sumaA.val", %"j.val.1"
  store i32 %"addtmp.2", i32* %"sumaA"
  %"sumaA.val.1" = load i32, i32* %"sumaA"
  %".45" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %"sumaA.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  br label %"while.cond.1"
while.cond.1:
  %"sumaA.val.2" = load i32, i32* %"sumaA"
  %"cmptmp.2" = icmp slt i32 %"sumaA.val.2", 20
  br i1 %"cmptmp.2", label %"while.body.1", label %"while.end.1"
while.body.1:
  %"sumaA.val.3" = load i32, i32* %"sumaA"
  %".51" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".52" = call i32 (i8*, ...) @"printf"(i8* %".51", i32 %"sumaA.val.3")
  br label %"while.cond.1"
while.end.1:
  %"call_calcularMultiplicacionA" = call i32 @"calcularMultiplicacionA"(i32 5, i32 7)
  %"call_calcularPromedioA" = call double @"calcularPromedioA"(double 0x40424ccccccccccd, double 0x4018000000000000)
  %"parA" = alloca i1
  store i1 1, i1* %"parA"
  %".55" = icmp ne i32 0, 0
  br i1 %".55", label %"if.then.1", label %"if.else"
if.then.1:
  br label %"if.end.1"
if.end.1:
  %"y" = alloca i32
  store i32 0, i32* %"y"
  br label %"for.cond.1"
if.else:
  %"str.1.4_ptr" = getelementptr [19 x i8], [19 x i8]* @"str.1.4", i32 0, i32 0
  %".58" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i8* %"str.1.4_ptr")
  br label %"if.end.1"
for.cond.1:
  %"y.val" = load i32, i32* %"y"
  %"cmptmp.3" = icmp slt i32 %"y.val", 10000
  br i1 %"cmptmp.3", label %"for.body.1", label %"for.end.1"
for.body.1:
  %"sumaA2.val" = load i32, i32* %"sumaA2"
  %"y.val.1" = load i32, i32* %"y"
  %"addtmp.3" = add i32 %"sumaA2.val", %"y.val.1"
  store i32 %"addtmp.3", i32* %"sumaA2"
  %"sumaA2.val.1" = load i32, i32* %"sumaA2"
  %".65" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".66" = call i32 (i8*, ...) @"printf"(i8* %".65", i32 %"sumaA2.val.1")
  br label %"for.update.1"
for.update.1:
  br label %"for.cond.1"
for.end.1:
  %"numeroA21" = alloca i32
  store i32 31, i32* %"numeroA21"
  %"numeroA22" = alloca i32
  store i32 32, i32* %"numeroA22"
  %"numeroA23" = alloca i32
  store i32 33, i32* %"numeroA23"
  %"numeroA24" = alloca i32
  store i32 34, i32* %"numeroA24"
  %"numeroA25" = alloca i32
  store i32 35, i32* %"numeroA25"
  %"resultadonumeroA" = alloca i32
  %"addtmp.4" = add i32 31, 32
  store i32 %"addtmp.4", i32* %"resultadonumeroA"
  %"resultadonumeroA1" = alloca i32
  %"subtmp.1" = sub i32 32, 31
  store i32 %"subtmp.1", i32* %"resultadonumeroA1"
  %"resultadonumeroA2" = alloca i32
  %"multmp.2" = mul i32 33, 34
  store i32 %"multmp.2", i32* %"resultadonumeroA2"
  %"resultadonumeroA3" = alloca i32
  %"addtmp.5" = add i32 35, 35
  store i32 %"addtmp.5", i32* %"resultadonumeroA3"
  %"resultadonumeroA4" = alloca double
  %".78" = sitofp i32 2 to double
  %"divtmp.1" = fdiv double 0x4044400000000000, %".78"
  store double %"divtmp.1", double* %"resultadonumeroA4"
  %"call_calcularPromedioA2" = call double @"calcularPromedioA2"(double 0x4001d70a3d70a3d7, double 0x400a8f5c28f5c28f)
  %"contadorB" = alloca i32
  store i32 0, i32* %"contadorB"
  %"sumaB" = alloca i32
  store i32 0, i32* %"sumaB"
  %"sumaB2" = alloca i32
  store i32 0, i32* %"sumaB2"
  %"mensajeB" = alloca i8*
  %"str.1.5_ptr" = getelementptr [18 x i8], [18 x i8]* @"str.1.5", i32 0, i32 0
  store i8* %"str.1.5_ptr", i8** %"mensajeB"
  %"es_validoB" = alloca i1
  store i1 1, i1* %"es_validoB"
  %"es_adminB" = alloca i1
  store i1 0, i1* %"es_adminB"
  %"contadorB2" = alloca i32
  store i32 0, i32* %"contadorB2"
  %"sumaB3" = alloca i32
  store i32 0, i32* %"sumaB3"
  %"sumaB4" = alloca i32
  store i32 0, i32* %"sumaB4"
  %"mensajeB1" = alloca i8*
  %"mensajeB1_ptr_cast" = getelementptr [18 x i8], [18 x i8]* @"str.1.5", i32 0, i32 0
  store i8* %"mensajeB1_ptr_cast", i8** %"mensajeB1"
  %"es_validoB2" = alloca i1
  store i1 1, i1* %"es_validoB2"
  %"mensajeB.val" = load i8*, i8** %"mensajeB"
  %".91" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".92" = call i32 (i8*, ...) @"printf"(i8* %".91", i8* %"mensajeB.val")
  %"resultadoB1" = alloca i32
  %"addtmp.6" = add i32 7, 5
  store i32 %"addtmp.6", i32* %"resultadoB1"
  %"resultadoB2" = alloca i32
  %"subtmp.2" = sub i32 12, 4
  store i32 %"subtmp.2", i32* %"resultadoB2"
  %"resultadoB3" = alloca i32
  %"multmp.3" = mul i32 6, 9
  store i32 %"multmp.3", i32* %"resultadoB3"
  %"resultadoB4" = alloca double
  %"divtmp.2" = fdiv double 0x403e000000000000, 0x4018000000000000
  store double %"divtmp.2", double* %"resultadoB4"
  %"resultadoB1.val" = load i32, i32* %"resultadoB1"
  %".97" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".98" = call i32 (i8*, ...) @"printf"(i8* %".97", i32 %"resultadoB1.val")
  %"resultadoB2.val" = load i32, i32* %"resultadoB2"
  %".99" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".100" = call i32 (i8*, ...) @"printf"(i8* %".99", i32 %"resultadoB2.val")
  %"resultadoB3.val" = load i32, i32* %"resultadoB3"
  %".101" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".102" = call i32 (i8*, ...) @"printf"(i8* %".101", i32 %"resultadoB3.val")
  %"resultadoB4.val" = load double, double* %"resultadoB4"
  %".103" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".104" = call i32 (i8*, ...) @"printf"(i8* %".103", double %"resultadoB4.val")
  %"totalB" = alloca i32
  %"resultadoB1.val.1" = load i32, i32* %"resultadoB1"
  %"resultadoB2.val.1" = load i32, i32* %"resultadoB2"
  %"addtmp.7" = add i32 %"resultadoB1.val.1", %"resultadoB2.val.1"
  store i32 %"addtmp.7", i32* %"totalB"
  %"totalB2" = alloca i32
  %"resultadoB3.val.1" = load i32, i32* %"resultadoB3"
  %"resultadoB1.val.2" = load i32, i32* %"resultadoB1"
  %"multmp.4" = mul i32 %"resultadoB3.val.1", %"resultadoB1.val.2"
  store i32 %"multmp.4", i32* %"totalB2"
  %"totalB.val" = load i32, i32* %"totalB"
  %".107" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".108" = call i32 (i8*, ...) @"printf"(i8* %".107", i32 %"totalB.val")
  %".109" = icmp ne i32 0, 0
  br i1 %".109", label %"if.then.2", label %"if.end.2"
if.then.2:
  br label %"if.end.2"
if.end.2:
  %"k" = alloca i32
  store i32 0, i32* %"k"
  br label %"for.cond.2"
for.cond.2:
  %"k.val" = load i32, i32* %"k"
  %"cmptmp.4" = icmp slt i32 %"k.val", 19
  br i1 %"cmptmp.4", label %"for.body.2", label %"for.end.2"
for.body.2:
  %"sumaB.val" = load i32, i32* %"sumaB"
  %"k.val.1" = load i32, i32* %"k"
  %"addtmp.8" = add i32 %"sumaB.val", %"k.val.1"
  store i32 %"addtmp.8", i32* %"sumaB"
  %"sumaB.val.1" = load i32, i32* %"sumaB"
  %".116" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".117" = call i32 (i8*, ...) @"printf"(i8* %".116", i32 %"sumaB.val.1")
  br label %"for.update.2"
for.update.2:
  br label %"for.cond.2"
for.end.2:
  br label %"while.cond.2"
while.cond.2:
  %"sumaB.val.2" = load i32, i32* %"sumaB"
  %"cmptmp.5" = icmp slt i32 %"sumaB.val.2", 20
  br i1 %"cmptmp.5", label %"while.body.2", label %"while.end.2"
while.body.2:
  %"sumaB.val.3" = load i32, i32* %"sumaB"
  %".122" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".123" = call i32 (i8*, ...) @"printf"(i8* %".122", i32 %"sumaB.val.3")
  br label %"while.cond.2"
while.end.2:
  %"call_calcularMultiplicacionB" = call i32 @"calcularMultiplicacionB"(i32 6, i32 8)
  %"call_calcularPromedioB" = call double @"calcularPromedioB"(double 0x4042d9999999999a, double 0x401c000000000000)
  %"parB" = alloca i1
  store i1 1, i1* %"parB"
  %".126" = icmp ne i32 0, 0
  br i1 %".126", label %"if.then.3", label %"if.else.1"
if.then.3:
  br label %"if.end.3"
if.end.3:
  %"z" = alloca i32
  store i32 0, i32* %"z"
  br label %"for.cond.3"
if.else.1:
  %"str.1.6_ptr" = getelementptr [18 x i8], [18 x i8]* @"str.1.6", i32 0, i32 0
  %".129" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".130" = call i32 (i8*, ...) @"printf"(i8* %".129", i8* %"str.1.6_ptr")
  br label %"if.end.3"
for.cond.3:
  %"z.val" = load i32, i32* %"z"
  %"cmptmp.6" = icmp slt i32 %"z.val", 1000
  br i1 %"cmptmp.6", label %"for.body.3", label %"for.end.3"
for.body.3:
  %"sumaB2.val" = load i32, i32* %"sumaB2"
  %"z.val.1" = load i32, i32* %"z"
  %"addtmp.9" = add i32 %"sumaB2.val", %"z.val.1"
  store i32 %"addtmp.9", i32* %"sumaB2"
  %"sumaB2.val.1" = load i32, i32* %"sumaB2"
  %".136" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".137" = call i32 (i8*, ...) @"printf"(i8* %".136", i32 %"sumaB2.val.1")
  br label %"for.update.3"
for.update.3:
  br label %"for.cond.3"
for.end.3:
  %"numeroB21" = alloca i32
  store i32 41, i32* %"numeroB21"
  %"numeroB22" = alloca i32
  store i32 42, i32* %"numeroB22"
  %"numeroB23" = alloca i32
  store i32 43, i32* %"numeroB23"
  %"numeroB24" = alloca i32
  store i32 44, i32* %"numeroB24"
  %"numeroB25" = alloca i32
  store i32 45, i32* %"numeroB25"
  %"resultadonumeroB" = alloca i32
  %"addtmp.10" = add i32 41, 42
  store i32 %"addtmp.10", i32* %"resultadonumeroB"
  %"resultadonumeroB1" = alloca i32
  %"subtmp.3" = sub i32 42, 41
  store i32 %"subtmp.3", i32* %"resultadonumeroB1"
  %"resultadonumeroB2" = alloca i32
  %"multmp.5" = mul i32 43, 44
  store i32 %"multmp.5", i32* %"resultadonumeroB2"
  %"resultadonumeroB3" = alloca i32
  %"addtmp.11" = add i32 45, 45
  store i32 %"addtmp.11", i32* %"resultadonumeroB3"
  %"resultadonumeroB4" = alloca double
  %".149" = sitofp i32 2 to double
  %"divtmp.3" = fdiv double 0x4049400000000000, %".149"
  store double %"divtmp.3", double* %"resultadonumeroB4"
  %"call_calcularPromedioB2" = call double @"calcularPromedioB2"(double 0x400ab851eb851eb8, double 0x4011b851eb851eb8)
  %"contadorC" = alloca i32
  store i32 0, i32* %"contadorC"
  %"sumaC" = alloca i32
  store i32 0, i32* %"sumaC"
  %"sumaC2" = alloca i32
  store i32 0, i32* %"sumaC2"
  %"mensajeC" = alloca i8*
  %"str.1.7_ptr" = getelementptr [17 x i8], [17 x i8]* @"str.1.7", i32 0, i32 0
  store i8* %"str.1.7_ptr", i8** %"mensajeC"
  %"es_validoC" = alloca i1
  store i1 1, i1* %"es_validoC"
  %"es_adminC" = alloca i1
  store i1 0, i1* %"es_adminC"
  %"contadorC2" = alloca i32
  store i32 0, i32* %"contadorC2"
  %"sumaC3" = alloca i32
  store i32 0, i32* %"sumaC3"
  %"sumaC4" = alloca i32
  store i32 0, i32* %"sumaC4"
  %"mensajeC1" = alloca i8*
  %"mensajeC1_ptr_cast" = getelementptr [17 x i8], [17 x i8]* @"str.1.7", i32 0, i32 0
  store i8* %"mensajeC1_ptr_cast", i8** %"mensajeC1"
  %"es_validoC2" = alloca i1
  store i1 1, i1* %"es_validoC2"
  %"mensajeC.val" = load i8*, i8** %"mensajeC"
  %".162" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".163" = call i32 (i8*, ...) @"printf"(i8* %".162", i8* %"mensajeC.val")
  %"resultadoC1" = alloca i32
  %"addtmp.12" = add i32 8, 6
  store i32 %"addtmp.12", i32* %"resultadoC1"
  %"resultadoC2" = alloca i32
  %"subtmp.4" = sub i32 13, 5
  store i32 %"subtmp.4", i32* %"resultadoC2"
  %"resultadoC3" = alloca i32
  %"multmp.6" = mul i32 7, 10
  store i32 %"multmp.6", i32* %"resultadoC3"
  %"resultadoC4" = alloca double
  %"divtmp.4" = fdiv double 0x4041800000000000, 0x401c000000000000
  store double %"divtmp.4", double* %"resultadoC4"
  %"resultadoC1.val" = load i32, i32* %"resultadoC1"
  %".168" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".169" = call i32 (i8*, ...) @"printf"(i8* %".168", i32 %"resultadoC1.val")
  %"resultadoC2.val" = load i32, i32* %"resultadoC2"
  %".170" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".171" = call i32 (i8*, ...) @"printf"(i8* %".170", i32 %"resultadoC2.val")
  %"resultadoC3.val" = load i32, i32* %"resultadoC3"
  %".172" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".173" = call i32 (i8*, ...) @"printf"(i8* %".172", i32 %"resultadoC3.val")
  %"resultadoC4.val" = load double, double* %"resultadoC4"
  %".174" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".175" = call i32 (i8*, ...) @"printf"(i8* %".174", double %"resultadoC4.val")
  %"totalC" = alloca i32
  %"resultadoC1.val.1" = load i32, i32* %"resultadoC1"
  %"resultadoC2.val.1" = load i32, i32* %"resultadoC2"
  %"addtmp.13" = add i32 %"resultadoC1.val.1", %"resultadoC2.val.1"
  store i32 %"addtmp.13", i32* %"totalC"
  %"totalC2" = alloca i32
  %"resultadoC3.val.1" = load i32, i32* %"resultadoC3"
  %"resultadoC1.val.2" = load i32, i32* %"resultadoC1"
  %"multmp.7" = mul i32 %"resultadoC3.val.1", %"resultadoC1.val.2"
  store i32 %"multmp.7", i32* %"totalC2"
  %"totalC.val" = load i32, i32* %"totalC"
  %".178" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".179" = call i32 (i8*, ...) @"printf"(i8* %".178", i32 %"totalC.val")
  %".180" = icmp ne i32 0, 0
  br i1 %".180", label %"if.then.4", label %"if.end.4"
if.then.4:
  br label %"if.end.4"
if.end.4:
  %"l" = alloca i32
  store i32 0, i32* %"l"
  br label %"for.cond.4"
for.cond.4:
  %"l.val" = load i32, i32* %"l"
  %"cmptmp.7" = icmp slt i32 %"l.val", 19
  br i1 %"cmptmp.7", label %"for.body.4", label %"for.end.4"
for.body.4:
  %"sumaC.val" = load i32, i32* %"sumaC"
  %"l.val.1" = load i32, i32* %"l"
  %"addtmp.14" = add i32 %"sumaC.val", %"l.val.1"
  store i32 %"addtmp.14", i32* %"sumaC"
  %"sumaC.val.1" = load i32, i32* %"sumaC"
  %".187" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".188" = call i32 (i8*, ...) @"printf"(i8* %".187", i32 %"sumaC.val.1")
  br label %"for.update.4"
for.update.4:
  br label %"for.cond.4"
for.end.4:
  br label %"while.cond.3"
while.cond.3:
  %"sumaC.val.2" = load i32, i32* %"sumaC"
  %"cmptmp.8" = icmp slt i32 %"sumaC.val.2", 20
  br i1 %"cmptmp.8", label %"while.body.3", label %"while.end.3"
while.body.3:
  %"sumaC.val.3" = load i32, i32* %"sumaC"
  %".193" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".194" = call i32 (i8*, ...) @"printf"(i8* %".193", i32 %"sumaC.val.3")
  br label %"while.cond.3"
while.end.3:
  %"call_calcularMultiplicacionC" = call i32 @"calcularMultiplicacionC"(i32 7, i32 9)
  %"call_calcularPromedioC" = call double @"calcularPromedioC"(double 0x4043666666666666, double 0x4020000000000000)
  %"parC" = alloca i1
  store i1 1, i1* %"parC"
  %".197" = icmp ne i32 0, 0
  br i1 %".197", label %"if.then.5", label %"if.else.2"
if.then.5:
  br label %"if.end.5"
if.end.5:
  %"w" = alloca i32
  store i32 0, i32* %"w"
  br label %"for.cond.5"
if.else.2:
  %"str.1.8_ptr" = getelementptr [18 x i8], [18 x i8]* @"str.1.8", i32 0, i32 0
  %".200" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".201" = call i32 (i8*, ...) @"printf"(i8* %".200", i8* %"str.1.8_ptr")
  br label %"if.end.5"
for.cond.5:
  %"w.val" = load i32, i32* %"w"
  %"cmptmp.9" = icmp slt i32 %"w.val", 10000
  br i1 %"cmptmp.9", label %"for.body.5", label %"for.end.5"
for.body.5:
  %"sumaC2.val" = load i32, i32* %"sumaC2"
  %"w.val.1" = load i32, i32* %"w"
  %"addtmp.15" = add i32 %"sumaC2.val", %"w.val.1"
  store i32 %"addtmp.15", i32* %"sumaC2"
  %"sumaC2.val.1" = load i32, i32* %"sumaC2"
  %".207" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".208" = call i32 (i8*, ...) @"printf"(i8* %".207", i32 %"sumaC2.val.1")
  br label %"for.update.5"
for.update.5:
  br label %"for.cond.5"
for.end.5:
  %"numeroC21" = alloca i32
  store i32 51, i32* %"numeroC21"
  %"numeroC22" = alloca i32
  store i32 52, i32* %"numeroC22"
  %"numeroC23" = alloca i32
  store i32 53, i32* %"numeroC23"
  %"numeroC24" = alloca i32
  store i32 54, i32* %"numeroC24"
  %"numeroC25" = alloca i32
  store i32 55, i32* %"numeroC25"
  %"resultadonumeroC" = alloca i32
  %"addtmp.16" = add i32 51, 52
  store i32 %"addtmp.16", i32* %"resultadonumeroC"
  %"resultadonumeroC1" = alloca i32
  %"subtmp.5" = sub i32 52, 51
  store i32 %"subtmp.5", i32* %"resultadonumeroC1"
  %"resultadonumeroC2" = alloca i32
  %"multmp.8" = mul i32 53, 54
  store i32 %"multmp.8", i32* %"resultadonumeroC2"
  %"resultadonumeroC3" = alloca i32
  %"addtmp.17" = add i32 55, 55
  store i32 %"addtmp.17", i32* %"resultadonumeroC3"
  %"resultadonumeroC4" = alloca double
  %".220" = sitofp i32 2 to double
  %"divtmp.5" = fdiv double 0x404e400000000000, %".220"
  store double %"divtmp.5", double* %"resultadonumeroC4"
  %"call_calcularPromedioC2" = call double @"calcularPromedioC2"(double 0x4011cccccccccccd, double 0x401628f5c28f5c29)
  ret i32 0
}

@"str.1.0" = internal constant [18 x i8] c"Iniciando proceso\00"
@"fmt.1" = internal constant [4 x i8] c"%s\0a\00"
@"fmt.2" = internal constant [4 x i8] c"%d\0a\00"
@"fmt.3" = internal constant [4 x i8] c"%f\0a\00"
define i32 @"fibonacci"(i32 %".1")
{
entry:
  %"n.addr" = alloca i32
  store i32 %".1", i32* %"n.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i32 0
if.else:
  %"n.val" = load i32, i32* %"n.addr"
  %"subtmp" = sub i32 %"n.val", 1
  %"call_fibonacci" = call i32 @"fibonacci"(i32 %"subtmp")
  %"n.val.1" = load i32, i32* %"n.addr"
  %"subtmp.1" = sub i32 %"n.val.1", 2
  %"call_fibonacci.1" = call i32 @"fibonacci"(i32 %"subtmp.1")
  %"addtmp" = add i32 %"call_fibonacci", %"call_fibonacci.1"
  ret i32 %"addtmp"
}

define i32 @"calcularMultiplicacionA"(i32 %".1", i32 %".2")
{
entry:
  %"c.addr" = alloca i32
  store i32 %".1", i32* %"c.addr"
  %"d.addr" = alloca i32
  store i32 %".2", i32* %"d.addr"
  %"resultadoA" = alloca i32
  %"c.val" = load i32, i32* %"c.addr"
  %"d.val" = load i32, i32* %"d.addr"
  %"multmp" = mul i32 %"c.val", %"d.val"
  store i32 %"multmp", i32* %"resultadoA"
  %"resultadoA.val" = load i32, i32* %"resultadoA"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoA.val")
  %"resultadoA.val.1" = load i32, i32* %"resultadoA"
  ret i32 %"resultadoA.val.1"
}

define double @"calcularPromedioA"(double %".1", double %".2")
{
entry:
  %"totalA.addr" = alloca double
  store double %".1", double* %"totalA.addr"
  %"cantidadA.addr" = alloca double
  store double %".2", double* %"cantidadA.addr"
  %"promedioA" = alloca double
  %"totalA.val" = load double, double* %"totalA.addr"
  %"cantidadA.val" = load double, double* %"cantidadA.addr"
  %"divtmp" = fdiv double %"totalA.val", %"cantidadA.val"
  store double %"divtmp", double* %"promedioA"
  %"promedioA.val" = load double, double* %"promedioA"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioA.val")
  %"promedioA.val.1" = load double, double* %"promedioA"
  ret double %"promedioA.val.1"
}

define i1 @"esParFuncA"(i32 %".1")
{
entry:
  %"numeroA.addr" = alloca i32
  store i32 %".1", i32* %"numeroA.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i1 false
if.else:
  ret i1 0
}

@"str.1.4" = internal constant [19 x i8] c"El numero es impar\00"
define i32 @"calcularMultiplicacionA2"(i32 %".1", i32 %".2")
{
entry:
  %"c1.addr" = alloca i32
  store i32 %".1", i32* %"c1.addr"
  %"d2.addr" = alloca i32
  store i32 %".2", i32* %"d2.addr"
  %"resultadoA" = alloca i32
  %"c1.val" = load i32, i32* %"c1.addr"
  %"d2.val" = load i32, i32* %"d2.addr"
  %"multmp" = mul i32 %"c1.val", %"d2.val"
  store i32 %"multmp", i32* %"resultadoA"
  %"resultadoA.val" = load i32, i32* %"resultadoA"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoA.val")
  %"resultadoA.val.1" = load i32, i32* %"resultadoA"
  ret i32 %"resultadoA.val.1"
}

define double @"calcularPromedioA2"(double %".1", double %".2")
{
entry:
  %"totalA2.addr" = alloca double
  store double %".1", double* %"totalA2.addr"
  %"cantidadA2.addr" = alloca double
  store double %".2", double* %"cantidadA2.addr"
  %"promedioA" = alloca double
  %"totalA2.val" = load double, double* %"totalA2.addr"
  %"cantidadA2.val" = load double, double* %"cantidadA2.addr"
  %"divtmp" = fdiv double %"totalA2.val", %"cantidadA2.val"
  store double %"divtmp", double* %"promedioA"
  %"promedioA.val" = load double, double* %"promedioA"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioA.val")
  %"promedioA.val.1" = load double, double* %"promedioA"
  ret double %"promedioA.val.1"
}

define double @"calcularPromedioA3"(i32 %".1")
{
entry:
  %"y.addr" = alloca i32
  store i32 %".1", i32* %"y.addr"
  %"sumaA32" = alloca i32
  store i32 0, i32* %"sumaA32"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  br label %"for.cond"
for.cond:
  %"j.val" = load i32, i32* %"j"
  %"cmptmp" = icmp slt i32 %"j.val", 10000
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"sumaA32.val" = load i32, i32* %"sumaA32"
  %"j.val.1" = load i32, i32* %"j"
  %"addtmp" = add i32 %"sumaA32.val", %"j.val.1"
  store i32 %"addtmp", i32* %"sumaA32"
  %"sumaA32.val.1" = load i32, i32* %"sumaA32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaA32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}

@"str.1.5" = internal constant [18 x i8] c"Ejecutando rutina\00"
define i32 @"calcularMultiplicacionB"(i32 %".1", i32 %".2")
{
entry:
  %"e.addr" = alloca i32
  store i32 %".1", i32* %"e.addr"
  %"f.addr" = alloca i32
  store i32 %".2", i32* %"f.addr"
  %"resultadoB" = alloca i32
  %"e.val" = load i32, i32* %"e.addr"
  %"f.val" = load i32, i32* %"f.addr"
  %"multmp" = mul i32 %"e.val", %"f.val"
  store i32 %"multmp", i32* %"resultadoB"
  %"resultadoB.val" = load i32, i32* %"resultadoB"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoB.val")
  %"resultadoB.val.1" = load i32, i32* %"resultadoB"
  ret i32 %"resultadoB.val.1"
}

define double @"calcularPromedioB"(double %".1", double %".2")
{
entry:
  %"totalB.addr" = alloca double
  store double %".1", double* %"totalB.addr"
  %"cantidadB.addr" = alloca double
  store double %".2", double* %"cantidadB.addr"
  %"promedioB" = alloca double
  %"totalB.val" = load double, double* %"totalB.addr"
  %"cantidadB.val" = load double, double* %"cantidadB.addr"
  %"divtmp" = fdiv double %"totalB.val", %"cantidadB.val"
  store double %"divtmp", double* %"promedioB"
  %"promedioB.val" = load double, double* %"promedioB"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioB.val")
  %"promedioB.val.1" = load double, double* %"promedioB"
  ret double %"promedioB.val.1"
}

define i1 @"esParFuncB"(i32 %".1")
{
entry:
  %"numeroB.addr" = alloca i32
  store i32 %".1", i32* %"numeroB.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i1 false
if.else:
  ret i1 0
}

@"str.1.6" = internal constant [18 x i8] c"El valor es impar\00"
define i32 @"calcularMultiplicacionB2"(i32 %".1", i32 %".2")
{
entry:
  %"e1.addr" = alloca i32
  store i32 %".1", i32* %"e1.addr"
  %"f2.addr" = alloca i32
  store i32 %".2", i32* %"f2.addr"
  %"resultadoB" = alloca i32
  %"e1.val" = load i32, i32* %"e1.addr"
  %"f2.val" = load i32, i32* %"f2.addr"
  %"multmp" = mul i32 %"e1.val", %"f2.val"
  store i32 %"multmp", i32* %"resultadoB"
  %"resultadoB.val" = load i32, i32* %"resultadoB"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoB.val")
  %"resultadoB.val.1" = load i32, i32* %"resultadoB"
  ret i32 %"resultadoB.val.1"
}

define double @"calcularPromedioB2"(double %".1", double %".2")
{
entry:
  %"totalB2.addr" = alloca double
  store double %".1", double* %"totalB2.addr"
  %"cantidadB2.addr" = alloca double
  store double %".2", double* %"cantidadB2.addr"
  %"promedioB" = alloca double
  %"totalB2.val" = load double, double* %"totalB2.addr"
  %"cantidadB2.val" = load double, double* %"cantidadB2.addr"
  %"divtmp" = fdiv double %"totalB2.val", %"cantidadB2.val"
  store double %"divtmp", double* %"promedioB"
  %"promedioB.val" = load double, double* %"promedioB"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioB.val")
  %"promedioB.val.1" = load double, double* %"promedioB"
  ret double %"promedioB.val.1"
}

define double @"calcularPromedioB3"(i32 %".1")
{
entry:
  %"z.addr" = alloca i32
  store i32 %".1", i32* %"z.addr"
  %"sumaB32" = alloca i32
  store i32 0, i32* %"sumaB32"
  %"k" = alloca i32
  store i32 0, i32* %"k"
  br label %"for.cond"
for.cond:
  %"k.val" = load i32, i32* %"k"
  %"cmptmp" = icmp slt i32 %"k.val", 10000
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"sumaB32.val" = load i32, i32* %"sumaB32"
  %"k.val.1" = load i32, i32* %"k"
  %"addtmp" = add i32 %"sumaB32.val", %"k.val.1"
  store i32 %"addtmp", i32* %"sumaB32"
  %"sumaB32.val.1" = load i32, i32* %"sumaB32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaB32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}

@"str.1.7" = internal constant [17 x i8] c"Procesando datos\00"
define i32 @"calcularMultiplicacionC"(i32 %".1", i32 %".2")
{
entry:
  %"g.addr" = alloca i32
  store i32 %".1", i32* %"g.addr"
  %"h.addr" = alloca i32
  store i32 %".2", i32* %"h.addr"
  %"resultadoC" = alloca i32
  %"g.val" = load i32, i32* %"g.addr"
  %"h.val" = load i32, i32* %"h.addr"
  %"multmp" = mul i32 %"g.val", %"h.val"
  store i32 %"multmp", i32* %"resultadoC"
  %"resultadoC.val" = load i32, i32* %"resultadoC"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoC.val")
  %"resultadoC.val.1" = load i32, i32* %"resultadoC"
  ret i32 %"resultadoC.val.1"
}

define double @"calcularPromedioC"(double %".1", double %".2")
{
entry:
  %"totalC.addr" = alloca double
  store double %".1", double* %"totalC.addr"
  %"cantidadC.addr" = alloca double
  store double %".2", double* %"cantidadC.addr"
  %"promedioC" = alloca double
  %"totalC.val" = load double, double* %"totalC.addr"
  %"cantidadC.val" = load double, double* %"cantidadC.addr"
  %"divtmp" = fdiv double %"totalC.val", %"cantidadC.val"
  store double %"divtmp", double* %"promedioC"
  %"promedioC.val" = load double, double* %"promedioC"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioC.val")
  %"promedioC.val.1" = load double, double* %"promedioC"
  ret double %"promedioC.val.1"
}

define i1 @"esParFuncC"(i32 %".1")
{
entry:
  %"numeroC.addr" = alloca i32
  store i32 %".1", i32* %"numeroC.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i1 false
if.else:
  ret i1 0
}

@"str.1.8" = internal constant [18 x i8] c"La cifra es impar\00"
define i32 @"calcularMultiplicacionC2"(i32 %".1", i32 %".2")
{
entry:
  %"g1.addr" = alloca i32
  store i32 %".1", i32* %"g1.addr"
  %"h2.addr" = alloca i32
  store i32 %".2", i32* %"h2.addr"
  %"resultadoC" = alloca i32
  %"g1.val" = load i32, i32* %"g1.addr"
  %"h2.val" = load i32, i32* %"h2.addr"
  %"multmp" = mul i32 %"g1.val", %"h2.val"
  store i32 %"multmp", i32* %"resultadoC"
  %"resultadoC.val" = load i32, i32* %"resultadoC"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoC.val")
  %"resultadoC.val.1" = load i32, i32* %"resultadoC"
  ret i32 %"resultadoC.val.1"
}

define double @"calcularPromedioC2"(double %".1", double %".2")
{
entry:
  %"totalC2.addr" = alloca double
  store double %".1", double* %"totalC2.addr"
  %"cantidadC2.addr" = alloca double
  store double %".2", double* %"cantidadC2.addr"
  %"promedioC" = alloca double
  %"totalC2.val" = load double, double* %"totalC2.addr"
  %"cantidadC2.val" = load double, double* %"cantidadC2.addr"
  %"divtmp" = fdiv double %"totalC2.val", %"cantidadC2.val"
  store double %"divtmp", double* %"promedioC"
  %"promedioC.val" = load double, double* %"promedioC"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioC.val")
  %"promedioC.val.1" = load double, double* %"promedioC"
  ret double %"promedioC.val.1"
}

define double @"calcularPromedioC3"(i32 %".1")
{
entry:
  %"w.addr" = alloca i32
  store i32 %".1", i32* %"w.addr"
  %"sumaC32" = alloca i32
  store i32 0, i32* %"sumaC32"
  %"l" = alloca i32
  store i32 0, i32* %"l"
  br label %"for.cond"
for.cond:
  %"l.val" = load i32, i32* %"l"
  %"cmptmp" = icmp slt i32 %"l.val", 19
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"sumaC32.val" = load i32, i32* %"sumaC32"
  %"l.val.1" = load i32, i32* %"l"
  %"addtmp" = add i32 %"sumaC32.val", %"l.val.1"
  store i32 %"addtmp", i32* %"sumaC32"
  %"sumaC32.val.1" = load i32, i32* %"sumaC32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaC32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}
