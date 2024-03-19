def paciente_html(dados):
    html = f"""
        <table class="form">
            <tr trigger="cancel" class="editing">
                <td><input name="nome" value="{dados['nome']}"></td>
                <td><input name="email" value="{dados['email']}"></td>
                <td><input name="telefone" value="{dados['telefone']}"></td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Selecione</option>
                        <option value="aguardando">Aguardando</option>
                        <option value="em atendimento">Em atendimento</option>
                        <option value="internado">Internado</option>
                        <option value="liberado">Liberado</option>
                    </select>
                </td>
                <td class="icon">
                    <div>
                        <a class="button secondary" hx-get="/api/pacientes"
                            title="Cancelar a alteração"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Cancelar
                        </a>
                        <a class="button" hx-trigger="click" 
                            hx-include="closest tr"
                            hx-put="/api/pacientes/{dados['id']}" 
                            title="Salvar"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Salvar
                        </a>
                    </div>
                </td>
            </tr>
        </table>
        """
    return html


def medico_html(dados):
    html = f"""
        <table class="form">
            <tr trigger="cancel" class="editing">
                <td><input name="nome" value="{dados['nome']}"></td>
                <td><input name="crm" value="{dados['crm']}"></td>
                <td><input name="especialidade" value="{dados['especialidade']}"></td>
                <td>
                    <select name="turno">
                        <option value="" selected disabled hidden>Selecione</option>
                        <option value="diurno">Diurno</option>
                        <option value="vespertino">Vespertino</option>
                        <option value="noturno">Noturno</option>
                    </select>
                </td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Selecione</option>
                        <option value="em atendimento">Em atendimento</option>
                        <option value="em plantao">Em plantão</option>
                        <option value="indisponivel">Indisponível</option>
                    </select>
                </td>
                <td class="icon">
                    <div>
                        <a class= "button secondary" hx-get="/api/medicos"
                            title="Cancelar a alteração"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Cancelar
                        </a>
                        <a class="button" hx-trigger="click" 
                            hx-include="closest table"
                            hx-put="/api/medicos/{dados['id']}" 
                            title="Salvar"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Salvar
                        </a>
                    </div>
                </td>
            </tr>
        </table>
        """
    return html
