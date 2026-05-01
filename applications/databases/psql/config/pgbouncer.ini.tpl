{{ $host := .host | splitList ":" | first }}
{{ $port := .host | splitList ":" | last }}
[databases]
defaultdb = host={{ $host }} port={{ $port }}
{{- range $key, $val := . }}
{{- if ne $key "host" }}
{{ $key }} = host={{ $host }} port={{ $port }}
{{- end }}
{{- end }}

[users]

[pgbouncer]
listen_addr = *
listen_port = 5432
auth_file = /etc/pgbouncer/userlist.txt
admin_users = admin
server_reset_query = SELECT pg_advisory_unlock_all()
server_reset_query_always = 1
ignore_startup_parameters = extra_float_digits