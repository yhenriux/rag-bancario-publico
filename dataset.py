"""Constrói a amostra assistida e as passagens de referência sem gerar respostas."""
import json
from pathlib import Path
from study import records,write_records,write,validate_questions,digest

# Especificação autoral assistida por Codex. Não há anotadores humanos fictícios.
# (fase, id, família, classe, documento, pergunta, requisitos, âncoras, filtro)
SPECS=[
('pilot','I01','inter-age','direta','8f40','Qual é a faixa etária da Conta You do Inter?',['13 a 17 anos'],['13 à 17 anos'],{'product':['conta'],'public':['pf']}),
('pilot','I02','inter-card-fee','direta','48fd','O cartão de crédito do Inter possui anuidade?',['cartão de crédito sem anuidade'],['isento de anuidade'],{'product':['cartao']}),
('pilot','I03','inter-limit-cash','condicao','4e71','Tenho R$ 1.000 de limite de crédito disponível no Inter. Posso usar R$ 500 no Saque de Limite?',['até 20% do crédito disponível, limitado a R$ 2.000','R$ 500 excede 20% de R$ 1.000','encargos e elegibilidade permanecem sujeitos à análise'],['20% do seu limite de crédito','R$2.000,00','mediante análise de crédito'],{'product':['saque_limite']}),
('pilot','I04','inter-credit-request','condicao','e4a0','Na conta PF do Inter, preciso anexar documentos de renda para pedir a análise de crédito?',['documentos de renda são opcionais','solicitação pelo Super App, Cartões, Solicitar Análise de Crédito'],['não obrigatório','Solicitar Análise de Crédito'],{'product':['cartao'],'public':['pf']}),
('pilot','I05','inter-pix-cash','excecao','6668','Sou cliente PF do segmento Win no Inter. O limite de oito transações gratuitas de Pix Saque e Pix Troco vale para mim?',['Win possui operações ilimitadas e gratuitas','oito transações é cota compartilhada de PF Digital e MEI'],['8 transações gratuitas','PF do segmento One, Prime e Win'],{'product':['pix'],'public':['win']}),
('pilot','I06','inter-mei-pj','excecao','8f40','Sou MEI. Posso abrir a Conta Digital PJ comum do Inter em lugar da Conta MEI?',['a documentação informa que MEI não pode abrir conta PJ','há modalidade específica MEI'],['Cliente MEI não consegue abrir conta PJ','Conta Digital Microempreendedor'],{'product':['conta'],'public':['mei']}),
('pilot','I07','inter-age','ambiguidade','8f40','Sou menor de idade. Qual conta do Inter corresponde à minha idade?',['solicitar a idade','Kids e You correspondem a faixas diferentes'],['0 à 12 anos','13 à 17 anos'],{'product':['conta'],'public':['pf']}),
('pilot','I08','inter-pix-cash','ambiguidade','6668','Tenho conta Inter. Quantas operações de Pix Saque posso fazer gratuitamente por mês?',['pedir tipo de conta e segmento','cota e gratuidade variam conforme o público'],['8 transações gratuitas','Digital e Pro','Enterprise, Middle Market'],{'product':['pix']}),
('pilot','I09','inter-credit-request','insuficiencia','e4a0','Qual é o número máximo anual de pedidos de análise de crédito permitido pelo Inter?',['não há teto anual demonstrado na coleção','não inventar quantidade'],[],{'product':['cartao']}),
('pilot','I10','inter-absent-2027','insuficiencia','8f40','Qual é a tarifa de manutenção da Conta Constelação 2027 do Inter?',['produto e tarifa não localizados na coleção','declarar falta de evidência'],[],{'product':['conta']}),
('pilot','B01','bradesco-baskets','direta','34dd','Por quais canais posso contratar uma cesta de serviços do Bradesco?',['app Bradesco, caixas eletrônicos e Fone Fácil'],['Você pode contratar as cestas de serviços'],{'product':['conta']}),
('pilot','B02','bradesco-debit-unlock','direta','eb95','Como desbloquear pela primeira vez um cartão de débito Bradesco?',['caixa eletrônico Bradesco','senha de seis dígitos cadastrada na abertura'],['Desbloqueie','senha de 6'],{'product':['cartao']}),
('pilot','B03','bradesco-university','condicao','d78d','A conta universitária do Bradesco é gratuita para qualquer cesta de serviços?',['gratuidade declarada para cesta de serviços essenciais','não estender a todos os serviços'],['Conta gratuita válida para cesta de serviços essenciais'],{'product':['conta']}),
('pilot','B04','bradesco-flex','condicao','12ad','Tenho 17 anos e conta Bradesco. Atendo à idade mínima informada para o Crédito Flex?',['idade mínima é 18 anos','contratação sujeita à aprovação'],['idade mínima de 18 anos','Sujeito à aprovação de crédito'],{'product':['credito_flex']}),
('pilot','B05','bradesco-debit-replacement','excecao','0d75','Perdi meu cartão de débito Bradesco. A segunda via está incluída nos serviços essenciais gratuitos?',['perda é exceção à segunda via gratuita','não afirmar tarifa exata sem tabela'],['Segunda via do cartão de débito, exceto'],{'product':['conta'],'public':['pf']}),
('pilot','B06','bradesco-flex','excecao','12ad','Meu cartão American Express tradicional da linha compras pode integrar o Crédito Flex Bradesco?',['cartões American Express tradicionais das linhas crédito e compras estão excluídos'],['exceto Cartões American Express tradicionais'],{'product':['credito_flex']}),
('pilot','B07','bradesco-foreign-phone','ambiguidade','eb95','Estou no exterior. Para qual telefone do Bradesco devo ligar sobre meu cartão?',['pedir bandeira ou modalidade do cartão','há números distintos conforme cartão'],['Acesso do exterior','The Platinum Card'],{'product':['cartao']}),
('pilot','B08','bradesco-baskets','ambiguidade','34dd','Tenho uma conta Bradesco. Vou pagar mensalidade pela cesta?',['solicitar cesta contratada ou modalidade','há serviços essenciais e cestas distintas'],['Cestas de serviços e tarifas','Serviços essenciais'],{'product':['conta']}),
('pilot','B09','bradesco-absent-basket','insuficiencia','34dd','Qual é o preço da Cesta Constelação 2027 do Bradesco?',['cesta e preço não localizados na coleção','não inventar valor'],[],{'product':['conta']}),
('pilot','B10','bradesco-flex','insuficiencia','12ad','Qual é o limite máximo em reais que será aprovado para mim no Crédito Flex Bradesco?',['a coleção não determina limite individual','análise e aprovação não garantem valor pessoal'],[],{'product':['credito_flex']}),
('final','IF01','inter-card-delivery','direta','a748','Quais carteiras digitais são citadas para usar o cartão virtual PF do Inter enquanto o cartão físico não chega?',['Samsung Pay, Google Pay e Apple Pay','cartões virtuais PF e MEI podem ser cadastrados'],['Samsung Pay','Google Pay','Apple Pay','PF e MEI'],{'product':['cartao'],'public':['pf']}),
('final','IF02','inter-guarantee-redemption','condicao','1967','Apliquei há mais de um dia útil no CDB Mais Limite do Inter. O dinheiro garante compras no cartão e paguei a fatura hoje em outro banco. Qual prazo a documentação informa para liberar o resgate?',['é necessário pagar a fatura para liberar o valor comprometido','até dois dias úteis após pagamento','pagamento por outro banco pode acrescentar um dia'],['É necessário pagar a fatura','até 2 dias úteis','mais 1 dia'],{'product':['mais_limite']}),
('final','IF03','inter-loop','excecao','6144','Sou cliente Win do Inter. Preciso manter débito automático ativo para ganhar pontos Loop ao pagar a fatura?',['Win é exceção à exigência de débito automático','demais critérios de pagamento continuam pertinentes'],['exceto para clientes segmento Win e PJ','valor total da fatura','após a data de vencimento'],{'product':['loop'],'public':['win']}),
('final','IF04','inter-dispute','ambiguidade','e7fd','Quero contestar uma compra no cartão Inter. Quanto tempo tenho?',['pedir motivo da contestação e data da compra','compra desconhecida e produto não recebido têm orientações diferentes'],['45 dias'],{'product':['cartao']}),
('final','IF05','inter-absent-exchange','insuficiencia','8f40','Qual é a taxa de câmbio garantida por dez anos na Conta Órbita 2030 do Inter?',['produto e garantia não encontrados na coleção','não inventar câmbio'],[],{'product':['conta']}),
('final','BF01','bradesco-aeternum-additional','direta','7c84','Quantos cartões adicionais são informados para o Visa Aeternum Bradesco?',['até cinco cartões adicionais'],['São até 5 cartões adicionais'],{'product':['aeternum']}),
('final','BF02','bradesco-international-account','condicao','0c02','Já tenho conta-poupança Bradesco. A página de contas informa que posso solicitar a My Account internacional?',['correntista ou titular de conta-poupança Bradesco pode solicitar','não afirmar aprovação garantida'],['Se você já tem uma conta-corrente ou conta-poupança Bradesco'],{'product':['conta']}),
('final','BF03','bradesco-card-bill-payment','excecao','0489','Tenho um cartão Visa Fácil Bradesco. Ele é elegível para pagar contas de consumo usando o cartão?',['Visa Fácil está entre os cartões não elegíveis'],['Cartões não elegíveis','Visa Fácil'],{'product':['cartao']}),
('final','BF04','bradesco-aeternum-fee','ambiguidade','7c84','Tenho investimentos no Bradesco. Minha anuidade do cartão está isenta?',['pedir cartão e valor/modalidades dos investimentos','o Visa Aeternum usa critério específico, não universalizar'],['R$ 5 milhões','exceto investimentos em ações'],{'product':['cartao']}),
('final','BF05','bradesco-absent-card','insuficiencia','7c84','Qual é a anuidade do Cartão Órbita 2030 do Bradesco?',['cartão e anuidade não localizados na coleção','não inventar valor'],[],{'product':['cartao']})]


def build(documents_path,chunks_path,output):
    docs=records(documents_path);chunks=records(chunks_path);out=Path(output)
    out.mkdir(parents=True,exist_ok=False);questions=[];dossiers=[];units=[];unit_map={c['id']:[] for c in chunks}
    for phase,ident,family,cls,dp,q,requirements,needles,attrs in SPECS:
        doc=next(d for d in docs if d['document_id'].startswith(dp)); references=[]
        for j,needle in enumerate(needles):
            found=False
            for s in doc['sections']:
                start=s['text'].lower().find(needle.lower())
                if start<0:continue
                end=start+len(needle)
                uid=family+'-'+digest(doc['document_id']+s['location']+str(start)+str(end))[:12]
                if not any(u['id']==uid for u in units):
                    units.append({'id':uid,'document_id':doc['document_id'],'location':s['location'],
                       'char_start':start,'char_end':end,'source_sha256':doc['sha256'],
                       'origin':'Codex_assisted_specification','human_validated':False})
                    for c in chunks:
                        if c['document_id']==doc['document_id'] and c['location']==s['location'] and c['char_start']<=start and c['char_end']>=end:
                            unit_map[c['id']].append(uid)
                references.append(uid);found=True;break
            if not found:raise ValueError('Âncora não localizada: '+ident+' '+needle)
        questions.append({'id':ident,'bank':doc['bank'],'family':family,'class':cls,'question':q,
           'query_attributes':attrs,'phase':phase,'origin':'Codex_assisted','human_validated':False})
        dossiers.append({'question_id':ident,'expected':'clarify' if cls=='ambiguidade' else 'abstain' if cls=='insuficiencia' else 'answer',
           'requirements':requirements,'reference_units':references,'sufficient_sets':[references] if references else [],
           'source_urls':[doc['final_url']],'origin':'Codex_assisted_before_generation','human_validated':False,
           'respondibility':'collection_absence_candidate' if cls=='insuficiencia' else 'assisted_supported'})
    pilot=[q for q in questions if q['phase']=='pilot'];final=[q for q in questions if q['phase']=='final']
    validate_questions(pilot);validate_questions(final,{q['family'] for q in pilot})
    assert max(sum(q['family']==f for q in pilot) for f in {q['family'] for q in pilot})<=3
    assert len({q['family'] for q in final})==len(final)
    for phase,qs in [('pilot',pilot),('final',final)]:
        write_records(out/(phase+'-questions.jsonl'),qs)
        write_records(out/(phase+'-dossiers.jsonl'),[d for d in dossiers if d['question_id'] in {q['id'] for q in qs}])
    write_records(out/'reference-units.jsonl',units);write(out/'unit-map.json',unit_map)
    write(out/'selection.json',{'pilot_questions':len(pilot),'final_questions':len(final),
      'pilot_families':sorted({q['family'] for q in pilot}),'final_families':sorted({q['family'] for q in final}),
      'reason_for_reduction':'Coleção pequena, famílias agrupadas por regra, sem multiplicar paráfrases para atingir 60. Prioriza cinco classes e famílias novas. Amostra de conveniência assistida, sem garantia de representatividade ou dimensionamento confirmatório.',
      'technical_family_excluded':'inter-atm-withdrawal','human_validated':False,
      'final_family_relation':'Benefícios de adicionais e anuidade do Aeternum são regras distintas no mesmo documento; a dependência documental residual é reportada.'})

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('documents');p.add_argument('chunks');p.add_argument('output');a=p.parse_args()
 build(a.documents,a.chunks,a.output)
