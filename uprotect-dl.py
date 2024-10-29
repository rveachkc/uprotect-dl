from typing import Self

from rv_script_lib import ScriptBase

class UnifiProtectDownloader(ScriptBase):

    PARSER_ARGPARSE_KWARGS = {
        "description": "Unifi Protect Video Archiver",
    }

    def run(self: Self):

        self.log.info("Hello World!")

if __name__ == "__main__":
    
    ui_dl = UnifiProtectDownloader()

    ui_dl.run()
