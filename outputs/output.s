	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
# %bb.0:                                # %entry
	xorl	%eax, %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
                                        # -- End function
	.globl	selectionSort                   # -- Begin function selectionSort
	.p2align	4, 0x90
	.type	selectionSort,@function
selectionSort:                          # @selectionSort
# %bb.0:                                # %entry
	xorl	%eax, %eax
	retq
.Lfunc_end1:
	.size	selectionSort, .Lfunc_end1-selectionSort
                                        # -- End function
	.section	".note.GNU-stack","",@progbits
