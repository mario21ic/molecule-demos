# Testing Ansible Playbooks with Molecule

Instalar requisitos:
```
$ pip install -r requirements.txt
```

## Ejecutar todo con un solo comando:
```
$ molecule test
```

## Ejecutar paso a paso:
### 1. Crear instancia
```
$ molecule create
$ molecule list
```

### 2. Aplicar playbook + idempotence y validar manualmente
```
$ molecule converge
$ molecule login
# ps fax
# apt list --installed | grep nginx
# exit
```

### 5. Ejecutar test
```
$ molecule verify
```

### 6. Destroy
```
$ molecule destroy
```


## Ejecutar todo sin terminar instancia:
```
molecule test --destroy never
molecule login
molecule destroy --all
```

## Ejecutar todo sin terminar instancia en AWS:
```
molecule test --destroy never -s aws
molecule login -s aws
molecule destroy --all
```
