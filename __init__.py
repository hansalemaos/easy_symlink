import os
from touchtouch import touch


def create_symlink(filepath, symlinkpath):
    if os.path.exists(symlinkpath):
        if not os.path.islink(symlinkpath):
            raise ValueError(f"{symlinkpath} exists already and it is not a symlink!")
        else:
            try:
                os.remove(symlinkpath)
            except Exception:
                pass
    else:
        touch(symlinkpath)
        try:
            os.remove(symlinkpath)
        except Exception:
            pass
    try:
        os.symlink(filepath, symlinkpath)
        return True
    except Exception:
        return False


