def paciente_html(dados):
    html = f"""
        <table class="form">
            <tr trigger="cancel" class="editing">
                <td><input name="nome" value="{dados['nome']}"></td>
                <td><input name="rg" value="{dados['rg']}"></td>
                <td><input name="cpf" value="{dados['cpf']}"></td>
                <td><input name="dt_nasc" value="{dados['dt_nasc']}"></td>
                <td><input name="telefone" value="{dados['telefone']}"></td>
                <td><input name="email" value="{dados['email']}"></td>
                <td>
                    <select name="sexo">
                        <option value="" selected disabled hidden>Sexo</option>
                        <option value="Feminino">Feminino</option>
                        <option value="Masculino">Masculino</option>
                    </select>
                </td>
                <td><input name="peso" value="{dados['peso']}"></td>
                <td><input name="altura" value="{dados['altura']}"></td>
                <td>
                    <select name="tp_sanguineo">
                        <option value="" selected disabled hidden>Tipo Sanguineo</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </td>
                <td><input name="cep" value="{dados['cep']}"></td>
                <td><input name="cidade" value="{dados['cidade']}"></td>
                <td>
                    <select name="uf">
                        <option value="" selected disabled hidden>Estado</option>
                        <option value="AC">AC</option>
                        <option value="AL">AL</option>
                        <option value="AM">AM</option>
                        <option value="AP">AP</option>
                        <option value="BA">BA</option>
                        <option value="CE">CE</option>
                        <option value="DF">DF</option>
                        <option value="ES">ES</option>
                        <option value="GO">GO</option>
                        <option value="MA">MA</option>
                        <option value="MG">MG</option>
                        <option value="MT">MT</option>
                        <option value="MS">MS</option>
                        <option value="PA">PA</option>
                        <option value="PB">PB</option>
                        <option value="PE">PE</option>
                        <option value="PI">PI</option>
                        <option value="PR">PR</option>
                        <option value="RJ">RJ</option>
                        <option value="RN">RN</option>
                        <option value="RO">RO</option>
                        <option value="RR">RR</option>
                        <option value="RS">RS</option>
                        <option value="SC">SC</option>
                        <option value="SE">SE</option>
                        <option value="SP">SP</option>
                        <option value="TO">TO</option>
                    </select>
                </td>
                <td><input name="logradouro" value="{dados['logradouro']}"></td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Status</option>
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
                            hx-include="closest table"
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
                <td>
                    <select name="especialidade">
                        <option value="" selected disabled hidden>Especialidade</option>
                        <option value="pscicologia">Pscicologia</option>
                        <option value="psciquiatria">Psciquiatria</option>
                        <option value="pscicanalise">Pscicanalise</option>
                    </select>
                </td>
                <td><input name="crm" value="{dados['crm']}"></td>
                <td><input name="rg" value="{dados['rg']}"></td>
                <td><input name="cpf" value="{dados['cpf']}"></td>
                <td><input name="dt_nasc" value="{dados['dt_nasc']}"></td>
                <td><input name="telefone" value="{dados['telefone']}"></td>
                <td><input name="email" value="{dados['email']}"></td>
                <td>
                    <select name="sexo">
                        <option value="" selected disabled hidden>Sexo</option>
                        <option value="Feminino">Feminino</option>
                        <option value="Masculino">Masculino</option>
                    </select>
                </td>
                <td>
                    <select name="turno">
                        <option value="" selected disabled hidden>Turno</option>
                        <option value="diurno">Diurno</option>
                        <option value="vespertino">Vespertino</option>
                        <option value="noturno">Noturno</option>
                    </select>
                </td>
                <td><input name="cep" value="{dados['cep']}"></td>
                <td><input name="cidade" value="{dados['cidade']}"></td>
                <td>
                    <select name="uf">
                        <option value="" selected disabled hidden>Estado</option>
                        <option value="AC">AC</option>
                        <option value="AL">AL</option>
                        <option value="AM">AM</option>
                        <option value="AP">AP</option>
                        <option value="BA">BA</option>
                        <option value="CE">CE</option>
                        <option value="DF">DF</option>
                        <option value="ES">ES</option>
                        <option value="GO">GO</option>
                        <option value="MA">MA</option>
                        <option value="MG">MG</option>
                        <option value="MT">MT</option>
                        <option value="MS">MS</option>
                        <option value="PA">PA</option>
                        <option value="PB">PB</option>
                        <option value="PE">PE</option>
                        <option value="PI">PI</option>
                        <option value="PR">PR</option>
                        <option value="RJ">RJ</option>
                        <option value="RN">RN</option>
                        <option value="RO">RO</option>
                        <option value="RR">RR</option>
                        <option value="RS">RS</option>
                        <option value="SC">SC</option>
                        <option value="SE">SE</option>
                        <option value="SP">SP</option>
                        <option value="TO">TO</option>
                    </select>
                </td>
                <td><input name="logradouro" value="{dados['logradouro']}"></td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Status</option>
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
