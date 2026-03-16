/**
 * API helper for FirstDay UAE
 * Handles communication with backend API
 */

import {
  RecommendationResponse,
  CostEstimateResponse,
  BankRecommendationResponse,
  ChecklistResponse,
  ApiError,
} from '@/types';

const BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1';

/**
 * Generic fetch wrapper with error handling
 */
async function apiFetch<T>(
  endpoint: string,
  options: RequestInit = {},
): Promise<T> {
  const url = `${BASE_URL}${endpoint}`;
  
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      const error: ApiError = await response.json().catch(() => ({
        detail: `HTTP ${response.status}`,
      }));
      throw new Error(error.detail || `API error: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    throw new Error(error instanceof Error ? error.message : 'Unknown API error');
  }
}

/**
 * Get neighborhood recommendations
 */
export async function getRecommendations(
  citySlug: string,
  workLocation: string,
  monthlySalary: number,
  monthlyBudget: number,
  lifestyle: string,
  transportPreference: string,
  preferredCommuteMinutes: number = 30,
): Promise<RecommendationResponse> {
  return apiFetch<RecommendationResponse>('/recommendations', {
    method: 'POST',
    body: JSON.stringify({
      city_slug: citySlug,
      work_location_text: workLocation,
      monthly_salary: monthlySalary,
      monthly_budget: monthlyBudget,
      lifestyle,
      transport_preference: transportPreference,
      preferred_commute_minutes: preferredCommuteMinutes,
    }),
  });
}

/**
 * Get cost estimate for a location
 */
export async function getCostEstimate(
  citySlug: string,
  monthlySalary: number,
  lifestyle: string,
  transportPreference: string,
  neighborhoodSlug?: string,
): Promise<CostEstimateResponse> {
  return apiFetch<CostEstimateResponse>('/cost-estimate', {
    method: 'POST',
    body: JSON.stringify({
      city_slug: citySlug,
      neighborhood_slug: neighborhoodSlug,
      monthly_salary: monthlySalary,
      lifestyle,
      transport_preference: transportPreference,
    }),
  });
}

/**
 * Get bank recommendations
 */
export async function getBankRecommendations(
  monthlySalary: number,
  remittanceNeed: 'low' | 'medium' | 'high',
  prefersDigitalBanking: boolean,
  wantsCreditCardRewards: boolean,
): Promise<BankRecommendationResponse> {
  return apiFetch<BankRecommendationResponse>('/bank-advisor', {
    method: 'POST',
    body: JSON.stringify({
      monthly_salary: monthlySalary,
      remittance_need: remittanceNeed,
      prefers_digital_banking: prefersDigitalBanking,
      wants_credit_card_rewards: wantsCreditCardRewards,
    }),
  });
}

/**
 * Get relocation checklist
 */
export async function getChecklist(citySlug?: string): Promise<ChecklistResponse> {
  return apiFetch<ChecklistResponse>('/checklist', {
    method: 'POST',
    body: JSON.stringify({
      city_slug: citySlug,
    }),
  });
}

/**
 * Health check endpoint
 */
export async function healthCheck(): Promise<{ status: string }> {
  return apiFetch<{ status: string }>('/health');
}
