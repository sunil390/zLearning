
````
  - name: Display multiple variables as dict
    debug:
      var: smpe_global_dsn ,  smpe_target_zone1

  - name: Display multiple variables as list 
    debug:
      msg: 
        - "{{ smpe_global_dsn }}"
        - "{{ smpe_target_zone1 }}"
```
