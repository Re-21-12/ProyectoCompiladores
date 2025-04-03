	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$0, 4(%rsp)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB0_1
# %bb.3:                                # %else.0
	cmpl	$2, 4(%rsp)
	jl	.LBB0_5
# %bb.4:                                # %then.1
	movl	$fmt.3, %edi
	movl	$3, %esi
	jmp	.LBB0_2
.LBB0_1:                                # %then.0
	movl	$fmt.2, %edi
	movl	$2, %esi
	jmp	.LBB0_2
.LBB0_5:                                # %else.1
	movl	$fmt.4, %edi
	movl	$4, %esi
.LBB0_2:                                # %ifcont
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	fmt.2,@object                   # @fmt.2
	.section	.rodata,"a",@progbits
fmt.2:
	.asciz	"%d\n"
	.size	fmt.2, 4

	.type	fmt.3,@object                   # @fmt.3
fmt.3:
	.asciz	"%d\n"
	.size	fmt.3, 4

	.type	fmt.4,@object                   # @fmt.4
fmt.4:
	.asciz	"%d\n"
	.size	fmt.4, 4

	.section	".note.GNU-stack","",@progbits
