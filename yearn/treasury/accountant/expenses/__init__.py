
from brownie import chain
from yearn.networks import Network
from yearn.treasury.accountant.classes import HashMatcher, TopLevelTxGroup
from yearn.treasury.accountant.expenses import (general, infrastructure,
                                                people, security)

OPEX_LABEL = "Operating Expenses"

expenses_txgroup = TopLevelTxGroup(OPEX_LABEL)

if chain.id == Network.Mainnet:
    team = expenses_txgroup.create_child("Team Payments", people.is_team_payment)
    team.create_child("Replenish Streams", people.is_stream_replenishment)

    expenses_txgroup.create_child("Coordinape", people.is_coordinape)
    expenses_txgroup.create_child("The 0.03%", people.is_0_03_percent)
    expenses_txgroup.create_child("SMS Discretionary Budget", general.is_sms_discretionary_budget)
    expenses_txgroup.create_child("Travel Reimbursements", general.is_travel_reimbursement)

    security_txgroup = expenses_txgroup.create_child("Security")
    security_txgroup.create_child("Bug Bounty", security.is_bug_bounty)
    security_txgroup.create_child("Anti-Spam Discord Bot", security.is_antispam_bot)
    audit_txgroup = security_txgroup.create_child("Audit")
    audit_txgroup.create_child("yAcademy", security.is_yacademy_audit)
    audit_txgroup.create_child("Unspecified Audit", security.is_other_audit)


    grants = expenses_txgroup.create_child("Grants")

    brand = grants.create_child("Brand Identity", HashMatcher(general.hashes['brand identity']).contains)
    design = grants.create_child("Design", HashMatcher(general.hashes["design"]).contains)
    
    website = grants.create_child("Website")
    ux = website.create_child("UX")
    testing = ux.create_child("Testing", HashMatcher(general.hashes["website"]["ux"]["testing"]).contains)

    grants.create_child("yGift Team Grant", people.is_ygift_grant)
    grants.create_child("Other Grants", people.is_other_grant)
    grants.create_child("2021 Bonus", HashMatcher(people.eoy_bonus_hashes).contains)

    infrastructure_txgroup = expenses_txgroup.create_child("Infrastructure")
    infrastructure_txgroup.create_child("Server Costs", infrastructure.is_servers)
    infrastructure_txgroup.create_child("Tenderly Subscription", infrastructure.is_tenderly)
    infrastructure_txgroup.create_child("Unspecified Infra", infrastructure.is_generic)