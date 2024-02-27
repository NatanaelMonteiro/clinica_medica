def paciente_html(dados):
    html = f"""
        <tr trigger="cancel" class="editing">
            <td><input name="nome" value="{dados['nome']}"></td>
            <td><input name="email" value="{dados['email']}"></td>
            <td><input name="telefone" value="{dados['telefone']}"></td>
            <td><input name="status" value="{dados['status']}"></td>
            <td class="icon">
                <div>
                    <a hx-get="/api/pacientes"
                        title="Cancelar a alteração"
                        hx-swap="outerHTML" 
                        hx-target="closest table">
                        <i class="material-symbols-outlined small-icon">undo</i>
                    </a>
                    <a hx-trigger="click" 
                        hx-include="closest tr"
                        hx-put="/api/pacientes/{dados['id']}" 
                        title="Salvar"
                        hx-swap="outerHTML" 
                        hx-target="closest table">
                        <i class="material-symbols-outlined small-icon">save</i>
                    </a>
                </div>
            </td>
        </tr>
        """
    return html

def medico_html(dados):
    html = f"""
        <tr trigger="cancel" class="editing">
            <td><input name="nome" value="{dados['nome']}"></td>
            <td><input name="crm" value="{dados['crm']}"></td>
            <td><input name="especialidade" value="{dados['especialidade']}"></td>
            <td><input name="turno" value="{dados['turno']}"></td>
            <td><input name="status" value="{dados['status']}"></td>
            <td class="icon">
                <div>
                    <a hx-get="/api/medicos"
                        title="Cancelar a alteração"
                        hx-swap="outerHTML" 
                        hx-target="closest table">
                        <i class="material-symbols-outlined small-icon">undo</i>
                    </a>
                    <a hx-trigger="click" 
                        hx-include="closest tr"
                        hx-put="/api/medicos/{dados['id']}" 
                        title="Salvar"
                        hx-swap="outerHTML" 
                        hx-target="closest table">
                        <i class="material-symbols-outlined small-icon">save</i>
                    </a>
                </div>
            </td>
        </tr>
        """
    return html
