def paciente_html():
    html = f"""
        <table class="form">
            <tr><td colspan="4"><h4>Cadastrar Médico</h4></td></tr>
            <tr trigger="cancel" class="editing">
                <td><input placeholder="Nome do paciente" name="nome" value=""></td>
                <td><input placeholder="RG do paciente" name="rg" value=""></td>
                <td><input placeholder="CPF do paciente" name="cpf" value=""></td>
                <td><input placeholder="Data de nascimento" name="dt_nasc" value=""></td>
                <td><input placeholder="Telefone" name="telefone" value=""></td>
                <td><input placeholder="E-mail do paciente" name="email" value=""></td>
                <td>
                    <select name="sexo">
                        <option value="" selected disabled hidden>Selecione o sexo</option>
                        <option value="feminino">Feminino</option>
                        <option value="masculino">Masculino</option>
                    </select>
                </td>
                <td><input placeholder="Peso" name="peso" value=""></td>
                <td><input placeholder="Altura" name="altura" value=""></td>
                <td>
                    <select name="tp_sanguineo">
                        <option value="" selected disabled hidden>Selecione o tipo sanguineo</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                    </select>
                </td>
                <td><input placeholder="CEP" name="cep" value=""></td>
                <td><input placeholder="Cidade" name="cidade" value=""></td>
                <td>
                    <select name="UF">
                        <option value="" selected disabled hidden>Selecione o estado</option>
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
                <td><input placeholder="Logradouro" name="logradouro" value=""></td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Selecione o status</option>
                        <option value="aguardando">Aguardando</option>
                        <option value="em atendimento">Em atendimento</option>
                        <option value="internado">Internado</option>
                        <option value="liberado">Liberado</option>
                    </select>
                </td>
                <td class="button">
                    <div>
                        <a class="button secondary" hx-get="/api/pacientes"
                            title="Cancelar a alteração"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Cancelar
                        </a>
                        <a class=button hx-trigger="click" 
                            hx-include="closest tr"
                            hx-post="/api/pacientes" 
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


def medico_html():
    html = f"""
        <table class="form">
            <tr><td colspan="4"><h4>Cadastrar Médico</h4></td></tr>
            <tr trigger="cancel" class="editing">
                <td><input placeholder="Nome do médicos" name="nome" value=""></td>
                <td>
                    <select name="especialidade">
                        <option value="" selected disabled hidden>Selecione a especialidade</option>
                        <option value="pscicologia">Pscicologia</option>
                        <option value="psciquiatria">Psciquiatria</option>
                        <option value="pscicanalise">Pscicanalise</option>
                    </select>
                </td>
                <td><input placeholder="CRM do médicos" name="crm" value=""></td>
                <td><input placeholder="RG do médicos" name="rg" value=""></td>
                <td><input placeholder="CPF do médicos" name="cpf" value=""></td>
                <td><input placeholder="Data de nascimento" name="dt_nasc" value=""></td>
                <td><input placeholder="Telefone" name="telefone" value=""></td>
                <td><input placeholder="E-mail do médicos" name="email" value=""></td>
                <td>
                    <select name="sexo">
                        <option value="" selected disabled hidden>Selecione o sexo</option>
                        <option value="feminino">Feminino</option>
                        <option value="masculino">Masculino</option>
                    </select>
                </td>
                <td>
                    <select name="turno">
                        <option value="" selected disabled hidden>Selecione o turno</option>
                        <option value="diurno">Diurno</option>
                        <option value="vespertino">Vespertino</option>
                        <option value="noturno">Noturno</option>
                    </select>
                </td>
                <td><input placeholder="CEP" name="cep" value=""></td>
                <td><input placeholder="Cidade" name="cidade" value=""></td>
                <td>
                    <select name="UF">
                        <option value="" selected disabled hidden>Selecione o estado</option>
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
                <td><input placeholder="Logradouro" name="logradouro" value=""></td>
                <td>
                    <select name="status">
                        <option value="" selected disabled hidden>Selecione o status</option>
                        <option value="em atendimento">Em atendimento</option>
                        <option value="em plantao">Em plantão</option>
                        <option value="indisponivel">Indisponível</option>
                    </select>
                </td>
                <td class="button">
                    <div>
                        <a class="button secondary" hx-get="/api/medicos"
                            title="Cancelar a alteração"
                            hx-swap="outerHTML" 
                            hx-target="closest table">
                            Cancelar
                        </a>
                        <a class="button" hx-trigger="click" 
                            hx-include="closest tr"
                            hx-post="/api/medicos" 
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
