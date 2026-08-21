class AiMarketingAgentCampaignLifecycleManagerClient:
    def plan_campaign(self, campaign_brief: dict = None, total_budget_usd: float = 50000.0) -> dict:
        campaign_brief = campaign_brief or {}
        goal = campaign_brief.get("goal", "generate 500 MQLs")
        alloc = {
            "LinkedIn Ads": round(total_budget_usd * 0.35, 2),
            "Google Search": round(total_budget_usd * 0.30, 2),
            "Content & SEO": round(total_budget_usd * 0.20, 2),
            "Email Sequences": round(total_budget_usd * 0.10, 2),
            "Reserve (Optimization)": round(total_budget_usd * 0.05, 2)
        }
        return {
            "campaign_plan": {"name": "Q3 Demand Gen", "goal": goal, "duration_weeks": 8, "phases": ["Awareness", "Consideration", "Conversion"]},
            "channel_budget_allocation": alloc,
            "projected_metrics": {"mqls": 520, "pipeline_usd": 1_850_000, "cpl_usd": 96.2, "roas": 37.0},
            "optimization_actions": [
                "Pause LinkedIn campaigns with CTR < 0.3% after day 7.",
                "Auto-shift 15% budget from underperforming channels to top performer at week 3.",
                "Trigger A/B test on landing page CTA if conversion rate < 2.5%."
            ]
        }
