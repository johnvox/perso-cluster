{{- range $key, $val := . }}
{{- if list "host" | has $key | not }}
"{{ $key }}" "{{$val}}"
{{- end }}
{{- end }}