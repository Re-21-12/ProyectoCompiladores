	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
# %bb.0:                                # %entry
	pushq	%rax
	movl	$fmt.0, %edi
	movl	$11, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
                                        # -- End function
	.type	fmt.0,@object                   # @fmt.0
	.section	.rodata,"a",@progbits
fmt.0:
	.asciz	"%d\n"
	.size	fmt.0, 4

	.section	".note.GNU-stack","",@progbits
