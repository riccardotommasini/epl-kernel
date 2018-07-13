from __future__ import absolute_import

from ipykernel.kernelapp import IPKernelApp
from traitlets import Dict

# -----------------------------------------------------------------------

class EPLKernelApp( IPKernelApp ):
    """
    The main kernel application, inheriting from the ipykernel
    """
    from .kernel import EPLKernel
    from .install import EPLKernelInstall, EPLKernelRemove
    kernel_class = EPLKernel

    # We override subcommands to add our own install & remove commands
    subcommands = Dict({                                                        
        'install': (EPLKernelInstall, 
                    EPLKernelInstall.description.splitlines()[0]), 
        'remove': (EPLKernelRemove, 
                   EPLKernelRemove.description.splitlines()[0]), 
    })


# -----------------------------------------------------------------------

def main():
    """
    This is the installed entry point
    """
    EPLKernelApp.launch_instance()

if __name__ == '__main__':
    main()
