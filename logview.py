import tkinter as tk
from tkinter import filedialog, scrolledtext
import threading
import time
import os

class ApacheLogViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Apache Log Viewer")
        self.root.geometry("800x500")

        # Botão para selecionar arquivo
        self.btn_open = tk.Button(root, text="Selecionar Log", command=self.select_log)
        self.btn_open.pack(pady=5)

        # Área de texto rolável
        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=100)
        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        # Variável para armazenar o caminho do log
        self.log_file = None
        self.running = False

    def select_log(self):
        self.log_file = filedialog.askopenfilename(title="Selecione o arquivo de log",
                                                   filetypes=[("Arquivos de Log", "*.log"), ("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if self.log_file:
            print(f"Arquivo selecionado: {self.log_file}")  # Mensagem de depuração
            self.running = True
            threading.Thread(target=self.update_log, daemon=True).start()

    def update_log(self):
        """ Atualiza a exibição do log em tempo real """
        try:
            with open(self.log_file, "r", encoding="utf-8", errors="ignore") as file:
                file.seek(0, os.SEEK_END)  # Vai para o final do arquivo
                while self.running:
                    line = file.readline()
                    if line:
                        print(f"Linha lida: {line.strip()}")  # Mensagem de depuração
                        self.log_text.insert(tk.END, line)
                        self.log_text.yview(tk.END)  # Rolagem automática
                    else:
                        time.sleep(1)  # Aguarda novas linhas
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")  # Mensagem de depuração

if __name__ == "__main__":
    root = tk.Tk()
    app = ApacheLogViewer(root)
    root.mainloop()
