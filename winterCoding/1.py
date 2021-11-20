def fight(c_hp, c_ad, c_df, monster):
    origin_c_hp = c_hp;
    m_name, m_exp, m_hp, m_ad, m_df = monster.split();
    m_exp = int(m_exp)
    m_hp = int(m_hp)
    m_ad = int(m_ad)
    m_df = int(m_df)
    
    c2m_damage = c_ad - m_df;
    m2c_damage = m_ad - c_df;
    
    attack_cnt = 0;
    
    while(1):
        attack_cnt += 1;
        
        # 1. player가 monster 공격.
        m_hp -= c2m_damage;
        
        # 1-1. monster 체력이 감소하지 않는 경우.
        if c2m_damage <= 0:
            return m_name, 0, m_exp;
        
        # 2. monster 체력이 0이하면 몬스터 사망, 전투 종료.
        if m_hp <= 0:
            return m_name, attack_cnt, m_exp;
        
        # 3. monster가 player 공격.
        c_hp -= m2c_damage;       
        
        # 4. player 체력이 0 이하면 player 사망, 전투 종료.
        if c_hp <= 0:
            return m_name, 0, m_exp;

        # 5. player 회복.
        c_hp = origin_c_hp;
    

def solution(character, monsters):
    results = [];
    c_hp, c_ad, c_df = map(int, character.split());
    
    for monster in monsters:
        m_name, attack_cnt, exp = fight(c_hp, c_ad, c_df, monster)
        if attack_cnt == 0:
            continue;
        exp_by_time = exp / attack_cnt;
        results.append([m_name, exp_by_time, exp])
    
    results.sort(reverse = True, key = lambda x: (x[1], x[2]));
    
    answer = results[0][0];
    
    return answer