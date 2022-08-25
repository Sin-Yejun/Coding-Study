class Solution:
    def interpret(self, command: str) -> str:
        cmd = command.replace('()','o')
        cmd = cmd.replace('(al)','al')
        return cmd
