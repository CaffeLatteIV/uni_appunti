# Ridirezione dell'input/output, pipes
**Ogni processo ha 3 stram**
- standard input (stdin)
- standard output (stdout)
- standard error (stderr)

**Es**:
Salva l'output di ls in file.txt
```bash
ls folder > file.txt 
```
appende in fondo al file.txt l'output di ls (non cancella il contenuto del file)
```bash
ls folder >> file.txt
```
```
```

Ridirezione stdout e stderr del comando rm al file `/dev/null`
```bash
rm file.txt >& /dev/null
```

## Alcuni comandi con regex
dentro ai backtick posso inserire comandi
```bash
echo data odierna: `date`
```

Posso usare regex:
```bash
ls *a
ls s[0-1][0-9]
```

