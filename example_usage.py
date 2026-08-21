from client import AiMarketingAgentCampaignLifecycleManagerClient

def main():
    client = AiMarketingAgentCampaignLifecycleManagerClient()
    brief = {"goal": "generate 400 MQLs", "product": "Flowmatic AI", "target": "VP Operations at mid-market SaaS"}
    res = client.plan_campaign(brief, 60000.0)
    plan = res["campaign_plan"]
    metrics = res["projected_metrics"]
    print(f"Campaign: {plan['name']} | Goal: {plan['goal']} | Duration: {plan['duration_weeks']} weeks")
    print(f"Projected: {metrics['mqls']} MQLs | Pipeline: ${metrics['pipeline_usd']:,} | ROAS: {metrics['roas']}x")
    print("Budget Allocation:")
    for ch, amt in res["channel_budget_allocation"].items():
        print(f"  {ch}: ${amt:,}")
    print("Optimization Actions:")
    for a in res["optimization_actions"]:
        print(f"  → {a}")

if __name__ == "__main__":
    main()
