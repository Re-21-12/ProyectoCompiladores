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
  store i32 6, i32* %"resultadoA1"
  %"resultadoA2" = alloca i32
  store i32 11, i32* %"resultadoA2"
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
  store i32 %"resultadoA1.val.1", i32* %"totalA"
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
  store i32 %"sumaA.val", i32* %"sumaA"
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
  store i32 %"sumaA2.val", i32* %"sumaA2"
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
  store i32 31, i32* %"resultadonumeroA"
  %"resultadonumeroA1" = alloca i32
  store i32 32, i32* %"resultadonumeroA1"
  %"resultadonumeroA2" = alloca i32
  %"multmp.2" = mul i32 33, 34
  store i32 %"multmp.2", i32* %"resultadonumeroA2"
  %"resultadonumeroA3" = alloca i32
  store i32 35, i32* %"resultadonumeroA3"
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
  store i32 7, i32* %"resultadoB1"
  %"resultadoB2" = alloca i32
  store i32 12, i32* %"resultadoB2"
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
  store i32 %"resultadoB1.val.1", i32* %"totalB"
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
  store i32 %"sumaB.val", i32* %"sumaB"
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
  store i32 %"sumaB2.val", i32* %"sumaB2"
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
  store i32 41, i32* %"resultadonumeroB"
  %"resultadonumeroB1" = alloca i32
  store i32 42, i32* %"resultadonumeroB1"
  %"resultadonumeroB2" = alloca i32
  %"multmp.5" = mul i32 43, 44
  store i32 %"multmp.5", i32* %"resultadonumeroB2"
  %"resultadonumeroB3" = alloca i32
  store i32 45, i32* %"resultadonumeroB3"
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
  store i32 8, i32* %"resultadoC1"
  %"resultadoC2" = alloca i32
  store i32 13, i32* %"resultadoC2"
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
  store i32 %"resultadoC1.val.1", i32* %"totalC"
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
  store i32 %"sumaC.val", i32* %"sumaC"
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
  store i32 %"sumaC2.val", i32* %"sumaC2"
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
  store i32 51, i32* %"resultadonumeroC"
  %"resultadonumeroC1" = alloca i32
  store i32 52, i32* %"resultadonumeroC1"
  %"resultadonumeroC2" = alloca i32
  %"multmp.8" = mul i32 53, 54
  store i32 %"multmp.8", i32* %"resultadonumeroC2"
  %"resultadonumeroC3" = alloca i32
  store i32 55, i32* %"resultadonumeroC3"
  %"resultadonumeroC4" = alloca double
  %".220" = sitofp i32 2 to double
  %"divtmp.5" = fdiv double 0x404e400000000000, %".220"
  store double %"divtmp.5", double* %"resultadonumeroC4"
  %"call_calcularPromedioC2" = call double @"calcularPromedioC2"(double 0x4011cccccccccccd, double 0x401628f5c28f5c29)
  %"contadorD" = alloca i32
  store i32 0, i32* %"contadorD"
  %"sumaD" = alloca i32
  store i32 0, i32* %"sumaD"
  %"sumaD2" = alloca i32
  store i32 0, i32* %"sumaD2"
  %"mensajeD" = alloca i8*
  %"str.1.9_ptr" = getelementptr [19 x i8], [19 x i8]* @"str.1.9", i32 0, i32 0
  store i8* %"str.1.9_ptr", i8** %"mensajeD"
  %"es_validoD" = alloca i1
  store i1 1, i1* %"es_validoD"
  %"es_adminD" = alloca i1
  store i1 0, i1* %"es_adminD"
  %"contadorD2" = alloca i32
  store i32 0, i32* %"contadorD2"
  %"sumaD3" = alloca i32
  store i32 0, i32* %"sumaD3"
  %"sumaD4" = alloca i32
  store i32 0, i32* %"sumaD4"
  %"mensajeD1" = alloca i8*
  %"str.1.10_ptr" = getelementptr [25 x i8], [25 x i8]* @"str.1.10", i32 0, i32 0
  store i8* %"str.1.10_ptr", i8** %"mensajeD1"
  %"es_validoD2" = alloca i1
  store i1 1, i1* %"es_validoD2"
  %"mensajeD.val" = load i8*, i8** %"mensajeD"
  %".233" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".234" = call i32 (i8*, ...) @"printf"(i8* %".233", i8* %"mensajeD.val")
  %"resultadoD1" = alloca i32
  store i32 9, i32* %"resultadoD1"
  %"resultadoD2" = alloca i32
  store i32 15, i32* %"resultadoD2"
  %"resultadoD3" = alloca i32
  %"multmp.9" = mul i32 4, 11
  store i32 %"multmp.9", i32* %"resultadoD3"
  %"resultadoD4" = alloca double
  %"divtmp.6" = fdiv double 0x4046000000000000, 0x4010000000000000
  store double %"divtmp.6", double* %"resultadoD4"
  %"resultadoD1.val" = load i32, i32* %"resultadoD1"
  %".239" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".240" = call i32 (i8*, ...) @"printf"(i8* %".239", i32 %"resultadoD1.val")
  %"resultadoD2.val" = load i32, i32* %"resultadoD2"
  %".241" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".242" = call i32 (i8*, ...) @"printf"(i8* %".241", i32 %"resultadoD2.val")
  %"resultadoD3.val" = load i32, i32* %"resultadoD3"
  %".243" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".244" = call i32 (i8*, ...) @"printf"(i8* %".243", i32 %"resultadoD3.val")
  %"resultadoD4.val" = load double, double* %"resultadoD4"
  %".245" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".246" = call i32 (i8*, ...) @"printf"(i8* %".245", double %"resultadoD4.val")
  %"totalD" = alloca i32
  %"resultadoD1.val.1" = load i32, i32* %"resultadoD1"
  store i32 %"resultadoD1.val.1", i32* %"totalD"
  %"totalD2" = alloca i32
  %"resultadoD3.val.1" = load i32, i32* %"resultadoD3"
  %"resultadoD1.val.2" = load i32, i32* %"resultadoD1"
  %"multmp.10" = mul i32 %"resultadoD3.val.1", %"resultadoD1.val.2"
  store i32 %"multmp.10", i32* %"totalD2"
  %"totalD.val" = load i32, i32* %"totalD"
  %".249" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".250" = call i32 (i8*, ...) @"printf"(i8* %".249", i32 %"totalD.val")
  %"call_factorial" = call i32 @"factorial"(i32 5)
  %".251" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".252" = call i32 (i8*, ...) @"printf"(i8* %".251", i32 %"call_factorial")
  %".253" = icmp ne i32 0, 0
  br i1 %".253", label %"if.then.6", label %"if.end.6"
if.then.6:
  br label %"if.end.6"
if.end.6:
  %"m" = alloca i32
  store i32 0, i32* %"m"
  br label %"for.cond.6"
for.cond.6:
  %"m.val" = load i32, i32* %"m"
  %"cmptmp.10" = icmp slt i32 %"m.val", 15
  br i1 %"cmptmp.10", label %"for.body.6", label %"for.end.6"
for.body.6:
  %"sumaD.val" = load i32, i32* %"sumaD"
  store i32 %"sumaD.val", i32* %"sumaD"
  %"sumaD.val.1" = load i32, i32* %"sumaD"
  %".260" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".261" = call i32 (i8*, ...) @"printf"(i8* %".260", i32 %"sumaD.val.1")
  br label %"for.update.6"
for.update.6:
  br label %"for.cond.6"
for.end.6:
  br label %"while.cond.4"
while.cond.4:
  %"sumaD.val.2" = load i32, i32* %"sumaD"
  %"cmptmp.11" = icmp slt i32 %"sumaD.val.2", 30
  br i1 %"cmptmp.11", label %"while.body.4", label %"while.end.4"
while.body.4:
  %"sumaD.val.3" = load i32, i32* %"sumaD"
  %".266" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".267" = call i32 (i8*, ...) @"printf"(i8* %".266", i32 %"sumaD.val.3")
  br label %"while.cond.4"
while.end.4:
  %"call_calcularMultiplicacionD" = call i32 @"calcularMultiplicacionD"(i32 8, i32 6)
  %"call_calcularPromedioD" = call double @"calcularPromedioD"(double 0x4048000000000000, double 0x4020000000000000)
  %"imparD" = alloca i1
  %"call_esImparFuncD" = call i1 @"esImparFuncD"(i32 7)
  store i1 %"call_esImparFuncD", i1* %"imparD"
  %".270" = icmp ne i32 0, 0
  br i1 %".270", label %"if.then.7", label %"if.else.3"
if.then.7:
  br label %"if.end.7"
if.end.7:
  %"n" = alloca i32
  store i32 0, i32* %"n"
  br label %"for.cond.7"
if.else.3:
  %"str.1.11_ptr" = getelementptr [17 x i8], [17 x i8]* @"str.1.11", i32 0, i32 0
  %".273" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".274" = call i32 (i8*, ...) @"printf"(i8* %".273", i8* %"str.1.11_ptr")
  br label %"if.end.7"
for.cond.7:
  %"n.val" = load i32, i32* %"n"
  %"cmptmp.12" = icmp slt i32 %"n.val", 5000
  br i1 %"cmptmp.12", label %"for.body.7", label %"for.end.7"
for.body.7:
  %"sumaD2.val" = load i32, i32* %"sumaD2"
  store i32 %"sumaD2.val", i32* %"sumaD2"
  %"sumaD2.val.1" = load i32, i32* %"sumaD2"
  %".280" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".281" = call i32 (i8*, ...) @"printf"(i8* %".280", i32 %"sumaD2.val.1")
  br label %"for.update.7"
for.update.7:
  br label %"for.cond.7"
for.end.7:
  %"numeroD21" = alloca i32
  store i32 61, i32* %"numeroD21"
  %"numeroD22" = alloca i32
  store i32 62, i32* %"numeroD22"
  %"numeroD23" = alloca i32
  store i32 63, i32* %"numeroD23"
  %"numeroD24" = alloca i32
  store i32 64, i32* %"numeroD24"
  %"numeroD25" = alloca i32
  store i32 65, i32* %"numeroD25"
  %"resultadonumeroD" = alloca i32
  store i32 61, i32* %"resultadonumeroD"
  %"resultadonumeroD1" = alloca i32
  store i32 62, i32* %"resultadonumeroD1"
  %"resultadonumeroD2" = alloca i32
  %"multmp.11" = mul i32 63, 64
  store i32 %"multmp.11", i32* %"resultadonumeroD2"
  %"resultadonumeroD3" = alloca i32
  store i32 65, i32* %"resultadonumeroD3"
  %"resultadonumeroD4" = alloca double
  %".293" = sitofp i32 2 to double
  %"divtmp.7" = fdiv double 0x4051a00000000000, %".293"
  store double %"divtmp.7", double* %"resultadonumeroD4"
  %"call_calcularPromedioD2" = call double @"calcularPromedioD2"(double 0x4016333333333333, double 0x401aa3d70a3d70a4)
  %"contadorE" = alloca i32
  store i32 0, i32* %"contadorE"
  %"sumaE" = alloca i32
  store i32 0, i32* %"sumaE"
  %"sumaE2" = alloca i32
  store i32 0, i32* %"sumaE2"
  %"mensajeE" = alloca i8*
  %"str.1.12_ptr" = getelementptr [19 x i8], [19 x i8]* @"str.1.12", i32 0, i32 0
  store i8* %"str.1.12_ptr", i8** %"mensajeE"
  %"es_validoE" = alloca i1
  store i1 1, i1* %"es_validoE"
  %"es_adminE" = alloca i1
  store i1 0, i1* %"es_adminE"
  %"contadorE2" = alloca i32
  store i32 0, i32* %"contadorE2"
  %"sumaE3" = alloca i32
  store i32 0, i32* %"sumaE3"
  %"sumaE4" = alloca i32
  store i32 0, i32* %"sumaE4"
  %"mensajeE1" = alloca i8*
  %"str.1.13_ptr" = getelementptr [25 x i8], [25 x i8]* @"str.1.13", i32 0, i32 0
  store i8* %"str.1.13_ptr", i8** %"mensajeE1"
  %"es_validoE2" = alloca i1
  store i1 1, i1* %"es_validoE2"
  %"mensajeE.val" = load i8*, i8** %"mensajeE"
  %".306" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".307" = call i32 (i8*, ...) @"printf"(i8* %".306", i8* %"mensajeE.val")
  %"resultadoE1" = alloca i32
  store i32 10, i32* %"resultadoE1"
  %"resultadoE2" = alloca i32
  store i32 18, i32* %"resultadoE2"
  %"resultadoE3" = alloca i32
  %"multmp.12" = mul i32 3, 12
  store i32 %"multmp.12", i32* %"resultadoE3"
  %"resultadoE4" = alloca double
  %"divtmp.8" = fdiv double 0x4042000000000000, 0x4008000000000000
  store double %"divtmp.8", double* %"resultadoE4"
  %"resultadoE1.val" = load i32, i32* %"resultadoE1"
  %".312" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".313" = call i32 (i8*, ...) @"printf"(i8* %".312", i32 %"resultadoE1.val")
  %"resultadoE2.val" = load i32, i32* %"resultadoE2"
  %".314" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".315" = call i32 (i8*, ...) @"printf"(i8* %".314", i32 %"resultadoE2.val")
  %"resultadoE3.val" = load i32, i32* %"resultadoE3"
  %".316" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".317" = call i32 (i8*, ...) @"printf"(i8* %".316", i32 %"resultadoE3.val")
  %"resultadoE4.val" = load double, double* %"resultadoE4"
  %".318" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".319" = call i32 (i8*, ...) @"printf"(i8* %".318", double %"resultadoE4.val")
  %"totalE" = alloca i32
  %"resultadoE1.val.1" = load i32, i32* %"resultadoE1"
  store i32 %"resultadoE1.val.1", i32* %"totalE"
  %"totalE2" = alloca i32
  %"resultadoE3.val.1" = load i32, i32* %"resultadoE3"
  %"resultadoE1.val.2" = load i32, i32* %"resultadoE1"
  %"multmp.13" = mul i32 %"resultadoE3.val.1", %"resultadoE1.val.2"
  store i32 %"multmp.13", i32* %"totalE2"
  %"totalE.val" = load i32, i32* %"totalE"
  %".322" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".323" = call i32 (i8*, ...) @"printf"(i8* %".322", i32 %"totalE.val")
  %".324" = icmp ne i32 0, 0
  br i1 %".324", label %"if.then.8", label %"if.end.8"
if.then.8:
  br label %"if.end.8"
if.end.8:
  %"p" = alloca i32
  store i32 0, i32* %"p"
  br label %"for.cond.8"
for.cond.8:
  %"p.val" = load i32, i32* %"p"
  %"cmptmp.13" = icmp slt i32 %"p.val", 10
  br i1 %"cmptmp.13", label %"for.body.8", label %"for.end.8"
for.body.8:
  %"sumaE.val" = load i32, i32* %"sumaE"
  store i32 %"sumaE.val", i32* %"sumaE"
  %"sumaE.val.1" = load i32, i32* %"sumaE"
  %".331" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".332" = call i32 (i8*, ...) @"printf"(i8* %".331", i32 %"sumaE.val.1")
  br label %"for.update.8"
for.update.8:
  br label %"for.cond.8"
for.end.8:
  br label %"while.cond.5"
while.cond.5:
  %"sumaE.val.2" = load i32, i32* %"sumaE"
  %"cmptmp.14" = icmp slt i32 %"sumaE.val.2", 25
  br i1 %"cmptmp.14", label %"while.body.5", label %"while.end.5"
while.body.5:
  %"sumaE.val.3" = load i32, i32* %"sumaE"
  %".337" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".338" = call i32 (i8*, ...) @"printf"(i8* %".337", i32 %"sumaE.val.3")
  br label %"while.cond.5"
while.end.5:
  %"call_calcularMultiplicacionE" = call i32 @"calcularMultiplicacionE"(i32 9, i32 5)
  %"call_calcularPromedioE" = call double @"calcularPromedioE"(double 0x4046800000000000, double 0x4022000000000000)
  %"parE" = alloca i1
  %"call_esParFuncE" = call i1 @"esParFuncE"(i32 8)
  store i1 %"call_esParFuncE", i1* %"parE"
  %".341" = icmp ne i32 0, 0
  br i1 %".341", label %"if.then.9", label %"if.else.4"
if.then.9:
  br label %"if.end.9"
if.end.9:
  %"q" = alloca i32
  store i32 0, i32* %"q"
  br label %"for.cond.9"
if.else.4:
  %".344" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".345" = call i32 (i8*, ...) @"printf"(i8* %".344", [19 x i8]* @"str.1.4")
  br label %"if.end.9"
for.cond.9:
  %"q.val" = load i32, i32* %"q"
  %"cmptmp.15" = icmp slt i32 %"q.val", 3000
  br i1 %"cmptmp.15", label %"for.body.9", label %"for.end.9"
for.body.9:
  %"sumaE2.val" = load i32, i32* %"sumaE2"
  store i32 %"sumaE2.val", i32* %"sumaE2"
  %"sumaE2.val.1" = load i32, i32* %"sumaE2"
  %".351" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".352" = call i32 (i8*, ...) @"printf"(i8* %".351", i32 %"sumaE2.val.1")
  br label %"for.update.9"
for.update.9:
  br label %"for.cond.9"
for.end.9:
  %"numeroE21" = alloca i32
  store i32 71, i32* %"numeroE21"
  %"numeroE22" = alloca i32
  store i32 72, i32* %"numeroE22"
  %"numeroE23" = alloca i32
  store i32 73, i32* %"numeroE23"
  %"numeroE24" = alloca i32
  store i32 74, i32* %"numeroE24"
  %"numeroE25" = alloca i32
  store i32 75, i32* %"numeroE25"
  %"resultadonumeroE" = alloca i32
  store i32 71, i32* %"resultadonumeroE"
  %"resultadonumeroE1" = alloca i32
  store i32 72, i32* %"resultadonumeroE1"
  %"resultadonumeroE2" = alloca i32
  %"multmp.14" = mul i32 73, 74
  store i32 %"multmp.14", i32* %"resultadonumeroE2"
  %"resultadonumeroE3" = alloca i32
  store i32 75, i32* %"resultadonumeroE3"
  %"resultadonumeroE4" = alloca double
  %".364" = sitofp i32 2 to double
  %"divtmp.9" = fdiv double 0x4054200000000000, %".364"
  store double %"divtmp.9", double* %"resultadonumeroE4"
  %"call_calcularPromedioE2" = call double @"calcularPromedioE2"(double 0x401aa3d70a3d70a4, double 0x401f147ae147ae14)
  %"asdf" = alloca i32
  store i32 0, i32* %"asdf"
  %"limite2" = alloca i32
  store i32 10, i32* %"limite2"
  br label %"while.cond.6"
while.cond.6:
  %"asdf.val" = load i32, i32* %"asdf"
  %"limite2.val" = load i32, i32* %"limite2"
  %"cmptmp.16" = icmp slt i32 %"asdf.val", %"limite2.val"
  br i1 %"cmptmp.16", label %"while.body.6", label %"while.end.6"
while.body.6:
  %"asdf.val.1" = load i32, i32* %"asdf"
  %"call_fibonacci.1" = call i32 @"fibonacci"(i32 %"asdf.val.1")
  %".370" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".371" = call i32 (i8*, ...) @"printf"(i8* %".370", i32 %"call_fibonacci.1")
  br label %"while.cond.6"
while.end.6:
  %"indiceFibo" = alloca i32
  store i32 10, i32* %"indiceFibo"
  %"limiteFibo" = alloca i32
  store i32 30, i32* %"limiteFibo"
  br label %"while.cond.7"
while.cond.7:
  %"indiceFibo.val" = load i32, i32* %"indiceFibo"
  %"limiteFibo.val" = load i32, i32* %"limiteFibo"
  %"cmptmp.17" = icmp slt i32 %"indiceFibo.val", %"limiteFibo.val"
  br i1 %"cmptmp.17", label %"while.body.7", label %"while.end.7"
while.body.7:
  %"indiceFibo.val.1" = load i32, i32* %"indiceFibo"
  %"call_fibonacci.2" = call i32 @"fibonacci"(i32 %"indiceFibo.val.1")
  %".377" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".378" = call i32 (i8*, ...) @"printf"(i8* %".377", i32 %"call_fibonacci.2")
  br label %"while.cond.7"
while.end.7:
  %"iF" = alloca i32
  store i32 30, i32* %"iF"
  br label %"for.cond.10"
for.cond.10:
  %"iF.val" = load i32, i32* %"iF"
  %"cmptmp.18" = icmp slt i32 %"iF.val", 50
  br i1 %"cmptmp.18", label %"for.body.10", label %"for.end.10"
for.body.10:
  %"iF.val.1" = load i32, i32* %"iF"
  %"call_fibonacci.3" = call i32 @"fibonacci"(i32 %"iF.val.1")
  %".383" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".384" = call i32 (i8*, ...) @"printf"(i8* %".383", i32 %"call_fibonacci.3")
  br label %"for.update.10"
for.update.10:
  br label %"for.cond.10"
for.end.10:
  %"jF" = alloca i32
  store i32 50, i32* %"jF"
  br label %"while.cond.8"
while.cond.8:
  %"jF.val" = load i32, i32* %"jF"
  %"cmptmp.19" = icmp sle i32 %"jF.val", 60
  br i1 %"cmptmp.19", label %"while.body.8", label %"while.end.8"
while.body.8:
  %"jF.val.1" = load i32, i32* %"jF"
  %"call_fibonacci.4" = call i32 @"fibonacci"(i32 %"jF.val.1")
  %".390" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".391" = call i32 (i8*, ...) @"printf"(i8* %".390", i32 %"call_fibonacci.4")
  %"jF.val.2" = load i32, i32* %"jF"
  store i32 %"jF.val.2", i32* %"jF"
  br label %"while.cond.8"
while.end.8:
  %"asd2" = alloca i32
  store i32 0, i32* %"asd2"
  %"limite3" = alloca i32
  store i32 10000, i32* %"limite3"
  br label %"while.cond.9"
while.cond.9:
  %"asd2.val" = load i32, i32* %"asd2"
  %"limite3.val" = load i32, i32* %"limite3"
  %"cmptmp.20" = icmp slt i32 %"asd2.val", %"limite3.val"
  br i1 %"cmptmp.20", label %"while.body.9", label %"while.end.9"
while.body.9:
  %"asd2.val.1" = load i32, i32* %"asd2"
  %"modtmp" = srem i32 %"asd2.val.1", 30
  %"call_fibonacci.5" = call i32 @"fibonacci"(i32 %"modtmp")
  %".398" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".399" = call i32 (i8*, ...) @"printf"(i8* %".398", i32 %"call_fibonacci.5")
  br label %"while.cond.9"
while.end.9:
  %"indiceFibo2" = alloca i32
  store i32 10000, i32* %"indiceFibo2"
  %"limiteFibo2" = alloca i32
  store i32 20000, i32* %"limiteFibo2"
  br label %"while.cond.10"
while.cond.10:
  %"indiceFibo2.val" = load i32, i32* %"indiceFibo2"
  %"limiteFibo2.val" = load i32, i32* %"limiteFibo2"
  %"cmptmp.21" = icmp slt i32 %"indiceFibo2.val", %"limiteFibo2.val"
  br i1 %"cmptmp.21", label %"while.body.10", label %"while.end.10"
while.body.10:
  %"indiceFibo2.val.1" = load i32, i32* %"indiceFibo2"
  %"modtmp.1" = srem i32 %"indiceFibo2.val.1", 30
  %"call_fibonacci.6" = call i32 @"fibonacci"(i32 %"modtmp.1")
  %".405" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".406" = call i32 (i8*, ...) @"printf"(i8* %".405", i32 %"call_fibonacci.6")
  br label %"while.cond.10"
while.end.10:
  %"iF2" = alloca i32
  store i32 20000, i32* %"iF2"
  br label %"for.cond.11"
for.cond.11:
  %"iF2.val" = load i32, i32* %"iF2"
  %"cmptmp.22" = icmp slt i32 %"iF2.val", 30000
  br i1 %"cmptmp.22", label %"for.body.11", label %"for.end.11"
for.body.11:
  %"iF2.val.1" = load i32, i32* %"iF2"
  %"modtmp.2" = srem i32 %"iF2.val.1", 30
  %"call_fibonacci.7" = call i32 @"fibonacci"(i32 %"modtmp.2")
  %".411" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".412" = call i32 (i8*, ...) @"printf"(i8* %".411", i32 %"call_fibonacci.7")
  br label %"for.update.11"
for.update.11:
  br label %"for.cond.11"
for.end.11:
  %"jF2" = alloca i32
  store i32 30000, i32* %"jF2"
  br label %"while.cond.11"
while.cond.11:
  %"jF2.val" = load i32, i32* %"jF2"
  %"cmptmp.23" = icmp sle i32 %"jF2.val", 40000
  br i1 %"cmptmp.23", label %"while.body.11", label %"while.end.11"
while.body.11:
  %"jF2.val.1" = load i32, i32* %"jF2"
  %"modtmp.3" = srem i32 %"jF2.val.1", 30
  %"call_fibonacci.8" = call i32 @"fibonacci"(i32 %"modtmp.3")
  %".418" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".419" = call i32 (i8*, ...) @"printf"(i8* %".418", i32 %"call_fibonacci.8")
  %"jF2.val.2" = load i32, i32* %"jF2"
  store i32 %"jF2.val.2", i32* %"jF2"
  br label %"while.cond.11"
while.end.11:
  %"call_sumaRecursiva" = call i32 @"sumaRecursiva"(i32 5000)
  %".422" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".423" = call i32 (i8*, ...) @"printf"(i8* %".422", i32 %"call_sumaRecursiva")
  %"call_productoRecursivo" = call i32 @"productoRecursivo"(i32 100, i32 50)
  %".424" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".425" = call i32 (i8*, ...) @"printf"(i8* %".424", i32 %"call_productoRecursivo")
  %"call_potenciaRecursiva" = call i32 @"potenciaRecursiva"(i32 2, i32 20)
  %".426" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".427" = call i32 (i8*, ...) @"printf"(i8* %".426", i32 %"call_potenciaRecursiva")
  %"call_cuentaAtras" = call i32 @"cuentaAtras"(i32 1000)
  %"x2" = alloca i32
  store i32 0, i32* %"x2"
  br label %"for.cond.12"
for.cond.12:
  %"x2.val" = load i32, i32* %"x2"
  %"cmptmp.24" = icmp slt i32 %"x2.val", 10000
  br i1 %"cmptmp.24", label %"for.body.12", label %"for.end.12"
for.body.12:
  %"x2.val.1" = load i32, i32* %"x2"
  %"modtmp.4" = srem i32 %"x2.val.1", 20
  %"call_sumaRecursiva.1" = call i32 @"sumaRecursiva"(i32 %"modtmp.4")
  %".431" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".432" = call i32 (i8*, ...) @"printf"(i8* %".431", i32 %"call_sumaRecursiva.1")
  br label %"for.update.12"
for.update.12:
  br label %"for.cond.12"
for.end.12:
  %"y2" = alloca i32
  store i32 0, i32* %"y2"
  br label %"for.cond.13"
for.cond.13:
  %"y2.val" = load i32, i32* %"y2"
  %"cmptmp.25" = icmp slt i32 %"y2.val", 10000
  br i1 %"cmptmp.25", label %"for.body.13", label %"for.end.13"
for.body.13:
  %"y2.val.1" = load i32, i32* %"y2"
  %"modtmp.5" = srem i32 %"y2.val.1", 10
  %"call_productoRecursivo.1" = call i32 @"productoRecursivo"(i32 %"modtmp.5", i32 10)
  %".438" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".439" = call i32 (i8*, ...) @"printf"(i8* %".438", i32 %"call_productoRecursivo.1")
  br label %"for.update.13"
for.update.13:
  br label %"for.cond.13"
for.end.13:
  %"z2" = alloca i32
  store i32 0, i32* %"z2"
  br label %"for.cond.14"
for.cond.14:
  %"z2.val" = load i32, i32* %"z2"
  %"cmptmp.26" = icmp slt i32 %"z2.val", 10000
  br i1 %"cmptmp.26", label %"for.body.14", label %"for.end.14"
for.body.14:
  %"z2.val.1" = load i32, i32* %"z2"
  %"modtmp.6" = srem i32 %"z2.val.1", 10
  %"call_potenciaRecursiva.1" = call i32 @"potenciaRecursiva"(i32 3, i32 %"modtmp.6")
  %".445" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".446" = call i32 (i8*, ...) @"printf"(i8* %".445", i32 %"call_potenciaRecursiva.1")
  br label %"for.update.14"
for.update.14:
  br label %"for.cond.14"
for.end.14:
  %"sumaExtra1" = alloca i32
  store i32 0, i32* %"sumaExtra1"
  %"a" = alloca i32
  store i32 0, i32* %"a"
  br label %"for.cond.15"
for.cond.15:
  %"a.val" = load i32, i32* %"a"
  %"cmptmp.27" = icmp slt i32 %"a.val", 10000
  br i1 %"cmptmp.27", label %"for.body.15", label %"for.end.15"
for.body.15:
  %"sumaExtra1.val" = load i32, i32* %"sumaExtra1"
  store i32 %"sumaExtra1.val", i32* %"sumaExtra1"
  %"sumaExtra1.val.1" = load i32, i32* %"sumaExtra1"
  %".454" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".455" = call i32 (i8*, ...) @"printf"(i8* %".454", i32 %"sumaExtra1.val.1")
  br label %"for.update.15"
for.update.15:
  br label %"for.cond.15"
for.end.15:
  %"sumaExtra2" = alloca i32
  store i32 0, i32* %"sumaExtra2"
  %"b" = alloca i32
  store i32 0, i32* %"b"
  br label %"for.cond.16"
for.cond.16:
  %"b.val" = load i32, i32* %"b"
  %"cmptmp.28" = icmp slt i32 %"b.val", 10000
  br i1 %"cmptmp.28", label %"for.body.16", label %"for.end.16"
for.body.16:
  %"sumaExtra2.val" = load i32, i32* %"sumaExtra2"
  store i32 %"sumaExtra2.val", i32* %"sumaExtra2"
  %"sumaExtra2.val.1" = load i32, i32* %"sumaExtra2"
  %".463" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".464" = call i32 (i8*, ...) @"printf"(i8* %".463", i32 %"sumaExtra2.val.1")
  br label %"for.update.16"
for.update.16:
  br label %"for.cond.16"
for.end.16:
  %"sumaExtra3" = alloca i32
  store i32 0, i32* %"sumaExtra3"
  %"c" = alloca i32
  store i32 0, i32* %"c"
  br label %"for.cond.17"
for.cond.17:
  %"c.val" = load i32, i32* %"c"
  %"cmptmp.29" = icmp slt i32 %"c.val", 10000
  br i1 %"cmptmp.29", label %"for.body.17", label %"for.end.17"
for.body.17:
  %"sumaExtra3.val" = load i32, i32* %"sumaExtra3"
  store i32 %"sumaExtra3.val", i32* %"sumaExtra3"
  %"sumaExtra3.val.1" = load i32, i32* %"sumaExtra3"
  %".472" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".473" = call i32 (i8*, ...) @"printf"(i8* %".472", i32 %"sumaExtra3.val.1")
  br label %"for.update.17"
for.update.17:
  br label %"for.cond.17"
for.end.17:
  %"sumaExtra4" = alloca i32
  store i32 0, i32* %"sumaExtra4"
  %"d" = alloca i32
  store i32 0, i32* %"d"
  br label %"for.cond.18"
for.cond.18:
  %"d.val" = load i32, i32* %"d"
  %"cmptmp.30" = icmp slt i32 %"d.val", 10000
  br i1 %"cmptmp.30", label %"for.body.18", label %"for.end.18"
for.body.18:
  %"sumaExtra4.val" = load i32, i32* %"sumaExtra4"
  store i32 %"sumaExtra4.val", i32* %"sumaExtra4"
  %"sumaExtra4.val.1" = load i32, i32* %"sumaExtra4"
  %".481" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".482" = call i32 (i8*, ...) @"printf"(i8* %".481", i32 %"sumaExtra4.val.1")
  br label %"for.update.18"
for.update.18:
  br label %"for.cond.18"
for.end.18:
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
  %"call_fibonacci" = call i32 @"fibonacci"(i32 %"n.val")
  ret i32 %"call_fibonacci"
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
  store i32 %"sumaA32.val", i32* %"sumaA32"
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
  store i32 %"sumaB32.val", i32* %"sumaB32"
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
  store i32 %"sumaC32.val", i32* %"sumaC32"
  %"sumaC32.val.1" = load i32, i32* %"sumaC32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaC32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}

@"str.1.9" = internal constant [19 x i8] c"Inicio de rutina D\00"
@"str.1.10" = internal constant [25 x i8] c"Inicio de rutina D extra\00"
define i32 @"factorial"(i32 %".1")
{
entry:
  %"n.addr" = alloca i32
  store i32 %".1", i32* %"n.addr"
  %"resultadoF" = alloca i32
  store i32 1, i32* %"resultadoF"
  %"i" = alloca i32
  store i32 1, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.val" = load i32, i32* %"i"
  %"n.val" = load i32, i32* %"n.addr"
  %"cmptmp" = icmp sle i32 %"i.val", %"n.val"
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"resultadoF.val" = load i32, i32* %"resultadoF"
  %"i.val.1" = load i32, i32* %"i"
  %"multmp" = mul i32 %"resultadoF.val", %"i.val.1"
  store i32 %"multmp", i32* %"resultadoF"
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  %"resultadoF.val.1" = load i32, i32* %"resultadoF"
  ret i32 %"resultadoF.val.1"
}

define i32 @"calcularMultiplicacionD"(i32 %".1", i32 %".2")
{
entry:
  %"i.addr" = alloca i32
  store i32 %".1", i32* %"i.addr"
  %"j.addr" = alloca i32
  store i32 %".2", i32* %"j.addr"
  %"resultadoD" = alloca i32
  %"i.val" = load i32, i32* %"i.addr"
  %"j.val" = load i32, i32* %"j.addr"
  %"multmp" = mul i32 %"i.val", %"j.val"
  store i32 %"multmp", i32* %"resultadoD"
  %"resultadoD.val" = load i32, i32* %"resultadoD"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoD.val")
  %"resultadoD.val.1" = load i32, i32* %"resultadoD"
  ret i32 %"resultadoD.val.1"
}

define double @"calcularPromedioD"(double %".1", double %".2")
{
entry:
  %"totalD.addr" = alloca double
  store double %".1", double* %"totalD.addr"
  %"cantidadD.addr" = alloca double
  store double %".2", double* %"cantidadD.addr"
  %"promedioD" = alloca double
  %"totalD.val" = load double, double* %"totalD.addr"
  %"cantidadD.val" = load double, double* %"cantidadD.addr"
  %"divtmp" = fdiv double %"totalD.val", %"cantidadD.val"
  store double %"divtmp", double* %"promedioD"
  %"promedioD.val" = load double, double* %"promedioD"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioD.val")
  %"promedioD.val.1" = load double, double* %"promedioD"
  ret double %"promedioD.val.1"
}

define i1 @"esImparFuncD"(i32 %".1")
{
entry:
  %"numeroD.addr" = alloca i32
  store i32 %".1", i32* %"numeroD.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i1 false
if.else:
  ret i1 0
}

@"str.1.11" = internal constant [17 x i8] c"El numero es par\00"
define i32 @"calcularMultiplicacionD2"(i32 %".1", i32 %".2")
{
entry:
  %"i1.addr" = alloca i32
  store i32 %".1", i32* %"i1.addr"
  %"j2.addr" = alloca i32
  store i32 %".2", i32* %"j2.addr"
  %"resultadoD" = alloca i32
  %"i1.val" = load i32, i32* %"i1.addr"
  %"j2.val" = load i32, i32* %"j2.addr"
  %"multmp" = mul i32 %"i1.val", %"j2.val"
  store i32 %"multmp", i32* %"resultadoD"
  %"resultadoD.val" = load i32, i32* %"resultadoD"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoD.val")
  %"resultadoD.val.1" = load i32, i32* %"resultadoD"
  ret i32 %"resultadoD.val.1"
}

define double @"calcularPromedioD2"(double %".1", double %".2")
{
entry:
  %"totalD2.addr" = alloca double
  store double %".1", double* %"totalD2.addr"
  %"cantidadD2.addr" = alloca double
  store double %".2", double* %"cantidadD2.addr"
  %"promedioD" = alloca double
  %"totalD2.val" = load double, double* %"totalD2.addr"
  %"cantidadD2.val" = load double, double* %"cantidadD2.addr"
  %"divtmp" = fdiv double %"totalD2.val", %"cantidadD2.val"
  store double %"divtmp", double* %"promedioD"
  %"promedioD.val" = load double, double* %"promedioD"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioD.val")
  %"promedioD.val.1" = load double, double* %"promedioD"
  ret double %"promedioD.val.1"
}

define double @"calcularPromedioD3"(i32 %".1")
{
entry:
  %"n.addr" = alloca i32
  store i32 %".1", i32* %"n.addr"
  %"sumaD32" = alloca i32
  store i32 0, i32* %"sumaD32"
  %"m" = alloca i32
  store i32 0, i32* %"m"
  br label %"for.cond"
for.cond:
  %"m.val" = load i32, i32* %"m"
  %"cmptmp" = icmp slt i32 %"m.val", 5000
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"sumaD32.val" = load i32, i32* %"sumaD32"
  store i32 %"sumaD32.val", i32* %"sumaD32"
  %"sumaD32.val.1" = load i32, i32* %"sumaD32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaD32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}

@"str.1.12" = internal constant [19 x i8] c"Inicio de rutina E\00"
@"str.1.13" = internal constant [25 x i8] c"Inicio de rutina E extra\00"
define i32 @"calcularMultiplicacionE"(i32 %".1", i32 %".2")
{
entry:
  %"k.addr" = alloca i32
  store i32 %".1", i32* %"k.addr"
  %"l.addr" = alloca i32
  store i32 %".2", i32* %"l.addr"
  %"resultadoE" = alloca i32
  %"k.val" = load i32, i32* %"k.addr"
  %"l.val" = load i32, i32* %"l.addr"
  %"multmp" = mul i32 %"k.val", %"l.val"
  store i32 %"multmp", i32* %"resultadoE"
  %"resultadoE.val" = load i32, i32* %"resultadoE"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoE.val")
  %"resultadoE.val.1" = load i32, i32* %"resultadoE"
  ret i32 %"resultadoE.val.1"
}

define double @"calcularPromedioE"(double %".1", double %".2")
{
entry:
  %"totalE.addr" = alloca double
  store double %".1", double* %"totalE.addr"
  %"cantidadE.addr" = alloca double
  store double %".2", double* %"cantidadE.addr"
  %"promedioE" = alloca double
  %"totalE.val" = load double, double* %"totalE.addr"
  %"cantidadE.val" = load double, double* %"cantidadE.addr"
  %"divtmp" = fdiv double %"totalE.val", %"cantidadE.val"
  store double %"divtmp", double* %"promedioE"
  %"promedioE.val" = load double, double* %"promedioE"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioE.val")
  %"promedioE.val.1" = load double, double* %"promedioE"
  ret double %"promedioE.val.1"
}

define i1 @"esParFuncE"(i32 %".1")
{
entry:
  %"numeroE.addr" = alloca i32
  store i32 %".1", i32* %"numeroE.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i1 false
if.else:
  ret i1 0
}

define i32 @"calcularMultiplicacionE2"(i32 %".1", i32 %".2")
{
entry:
  %"k1.addr" = alloca i32
  store i32 %".1", i32* %"k1.addr"
  %"l2.addr" = alloca i32
  store i32 %".2", i32* %"l2.addr"
  %"resultadoE" = alloca i32
  %"k1.val" = load i32, i32* %"k1.addr"
  %"l2.val" = load i32, i32* %"l2.addr"
  %"multmp" = mul i32 %"k1.val", %"l2.val"
  store i32 %"multmp", i32* %"resultadoE"
  %"resultadoE.val" = load i32, i32* %"resultadoE"
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"resultadoE.val")
  %"resultadoE.val.1" = load i32, i32* %"resultadoE"
  ret i32 %"resultadoE.val.1"
}

define double @"calcularPromedioE2"(double %".1", double %".2")
{
entry:
  %"totalE2.addr" = alloca double
  store double %".1", double* %"totalE2.addr"
  %"cantidadE2.addr" = alloca double
  store double %".2", double* %"cantidadE2.addr"
  %"promedioE" = alloca double
  %"totalE2.val" = load double, double* %"totalE2.addr"
  %"cantidadE2.val" = load double, double* %"cantidadE2.addr"
  %"divtmp" = fdiv double %"totalE2.val", %"cantidadE2.val"
  store double %"divtmp", double* %"promedioE"
  %"promedioE.val" = load double, double* %"promedioE"
  %".7" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", double %"promedioE.val")
  %"promedioE.val.1" = load double, double* %"promedioE"
  ret double %"promedioE.val.1"
}

define double @"calcularPromedioE3"(i32 %".1")
{
entry:
  %"q.addr" = alloca i32
  store i32 %".1", i32* %"q.addr"
  %"sumaE32" = alloca i32
  store i32 0, i32* %"sumaE32"
  %"p" = alloca i32
  store i32 0, i32* %"p"
  br label %"for.cond"
for.cond:
  %"p.val" = load i32, i32* %"p"
  %"cmptmp" = icmp slt i32 %"p.val", 3000
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"sumaE32.val" = load i32, i32* %"sumaE32"
  store i32 %"sumaE32.val", i32* %"sumaE32"
  %"sumaE32.val.1" = load i32, i32* %"sumaE32"
  %".9" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"sumaE32.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret double              0x0
}

define i32 @"sumaRecursiva"(i32 %".1")
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
  ret i32 %"n.val"
}

define i32 @"productoRecursivo"(i32 %".1", i32 %".2")
{
entry:
  %"n.addr" = alloca i32
  store i32 %".1", i32* %"n.addr"
  %"m.addr" = alloca i32
  store i32 %".2", i32* %"m.addr"
  %".6" = icmp ne i32 0, 0
  br i1 %".6", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i32 0
if.else:
  %"n.val" = load i32, i32* %"n.addr"
  ret i32 %"n.val"
}

define i32 @"potenciaRecursiva"(i32 %".1", i32 %".2")
{
entry:
  %"base.addr" = alloca i32
  store i32 %".1", i32* %"base.addr"
  %"exp.addr" = alloca i32
  store i32 %".2", i32* %"exp.addr"
  %".6" = icmp ne i32 0, 0
  br i1 %".6", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i32 0
if.else:
  %"base.val" = load i32, i32* %"base.addr"
  %"base.val.1" = load i32, i32* %"base.addr"
  %"exp.val" = load i32, i32* %"exp.addr"
  %"call_potenciaRecursiva" = call i32 @"potenciaRecursiva"(i32 %"base.val.1", i32 %"exp.val")
  %"multmp" = mul i32 %"base.val", %"call_potenciaRecursiva"
  ret i32 %"multmp"
}

define i32 @"cuentaAtras"(i32 %".1")
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
  %".7" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"n.val")
  %"n.val.1" = load i32, i32* %"n.addr"
  %"call_cuentaAtras" = call i32 @"cuentaAtras"(i32 %"n.val.1")
  ret i32 %"call_cuentaAtras"
}
