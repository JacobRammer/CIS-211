"""
Jacob Rammer
Compiler 2019 codegen_context
"""

from typing import List
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

"""
A container for the context information kept 
for assembly code generation while walking 
an abstract syntax tree. 

The context object is passed around from node to 
node during code generation. Having a context 
object, rather than a set of different pieces
of information passed around, isolates in one 
place several small design decisions:  How 
registers are allocated, how constants and variables
are declared, when and how the code is actually
emitted to the output file. 
"""


class Context(object):
    """
    The state of code generation
    """

    def __init__(self):
        # A table of integer constants to be declared at
        # the end of the source program.  The table maps
        # values to names, so that we can reuse them.
        self.consts = {}

        # A table of variables to be declared at
        # the end of the source program, with the
        # symbols used for them in the assembly code.
        self.vars = {}

        # Instructions in the source code, as a list of
        # strings.
        self.assm_lines = []

        # The available registers
        self.registers = [f"r{i}" for i in range(1, 15)]
