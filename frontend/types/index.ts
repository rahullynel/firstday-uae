/**
 * Shared types for FirstDay UAE frontend
 */

// City
export interface City {
  id: number;
  name: string;
  slug: string;
  country: string;
  currency: string;
  created_at: string;
}

// Neighborhood Recommendation
export interface RecommendedNeighborhood {
  id: number;
  name: string;
  avg_rent_min: number;
  avg_rent_max: number;
  score: number;
  affordability_score: number;
  commute_score: number;
  lifestyle_score: number;
  walkability_score: number;
  top_reasons: string[];
}

export interface RecommendationResponse {
  city_name: string;
  city_slug: string;
  recommendations: RecommendedNeighborhood[];
  explanation: string;
}

// Cost Estimate
export interface CostBreakdown {
  category: string;
  amount: number;
  base_cost: number;
  cost_index: number;
}

export interface CostEstimateResponse {
  city_name: string;
  neighborhood_name: string | null;
  monthly_salary: number;
  lifestyle: string;
  transport_preference: string;
  breakdown: CostBreakdown[];
  total_monthly_cost: number;
  monthly_savings: number;
  savings_percentage: number;
  comfort_score: number;
  explanation: string;
}

// Bank Recommendation
export interface ActiveBankOffer {
  id: number;
  title: string;
  description: string;
  source_url: string | null;
  valid_from: string;
  valid_to: string;
}

export interface BankRecommendationDetail {
  id: number;
  name: string;
  logo_url: string | null;
  remittance_score: number;
  digital_banking_score: number;
  branch_network_score: number;
  total_score: number;
  top_reasons: string[];
  active_offers: ActiveBankOffer[];
}

export interface BankRecommendationResponse {
  monthly_salary: number;
  remittance_need: string;
  prefers_digital_banking: boolean;
  wants_credit_card_rewards: boolean;
  recommendations: BankRecommendationDetail[];
  explanation: string;
}

// Relocation Checklist
export interface ChecklistItem {
  id: number;
  title: string;
  description: string | null;
  category: string;
  day_order: number;
  official_link: string | null;
}

export interface ChecklistGroup {
  period: string;
  items: ChecklistItem[];
}

export interface ChecklistResponse {
  city_name: string | null;
  city_slug: string | null;
  total_items: number;
  groups: ChecklistGroup[];
}

// API Response wrapper
export interface ApiResponse<T> {
  data: T;
  status: number;
  message?: string;
}

// Error response
export interface ApiError {
  detail: string;
  status_code?: number;
}
