reporting_chain = {
  'Alice': 'João',
  'Amanda': 'João',
  'Caio': 'Alice',
  'Bianca': 'Amanda',
  'João': 'Marcio',
  'Marcio': 'Roberta'
}

def get_reporting_chain(employee, reporting_chain):
  
  chain = []
  
  while employee:
      chain.append(employee)
      employee = reporting_chain.get(employee)
  return chain

def common_manager(emp1, emp2, reporting_chain):
  chain1 = get_reporting_chain(emp1, reporting_chain)
  chain2 = get_reporting_chain(emp2, reporting_chain)
  
  for manager in chain1:
    if manager in chain2:
      return manager


employee1 = 'Caio'
employee2 = 'Bianca'
the_common_manager = common_manager(employee1, employee2, reporting_chain)
print(f"The common manager is {the_common_manager}.")
