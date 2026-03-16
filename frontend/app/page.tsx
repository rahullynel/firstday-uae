'use client';

import Link from 'next/link';
import Image from 'next/image';

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="section bg-gradient-to-br from-blue-50 via-white to-cyan-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-2 gap-12 md:gap-16 items-center">
            <div className="animate-fade-in">
              <h1 className="text-5xl md:text-6xl font-bold text-slate-900 mb-6 leading-tight">
                Your Relocation Journey Starts Here
              </h1>
              <p className="text-xl md:text-2xl text-slate-600 mb-8 leading-relaxed">
                FirstDay UAE helps newcomers find the perfect neighborhood, understand living costs, choose the best bank, and settle into Abu Dhabi with confidence.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button className="btn-primary text-lg px-8 py-3">
                  Explore Now
                </button>
                <button className="btn-secondary text-lg px-8 py-3">
                  Learn More
                </button>
              </div>
              <p className="text-sm text-slate-500 mt-6">
                ✓ Free • ✓ Data-driven • ✓ Trusted by thousands
              </p>
            </div>
            <div className="hidden lg:block">
              <div className="relative w-full aspect-square bg-gradient-to-br from-blue-400 to-cyan-400 rounded-2xl shadow-xl overflow-hidden">
                <div className="absolute inset-0 bg-opacity-10 bg-white flex items-center justify-center">
                  <svg className="w-32 h-32 text-white opacity-50" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10.5 1.5H5.75A2.25 2.25 0 003.5 3.75v12.5A2.25 2.25 0 005.75 18.5h8.5a2.25 2.25 0 002.25-2.25V6.5M10.5 1.5v5h5M10.5 1.5H9.25A1.25 1.25 0 008 2.75v3.5A1.25 1.25 0 009.25 7.5h1.25" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="section">
        <div className="container-custom">
          <div className="section-title text-center">
            <h2 className="mb-4">Everything You Need to Relocate</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Comprehensive tools designed specifically for expats moving to Abu Dhabi
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: '🏘️',
                title: 'Smart Neighborhoods',
                description: 'Find neighborhoods that match your lifestyle, budget, and commute preferences',
              },
              {
                icon: '💰',
                title: 'Cost Calculator',
                description: 'Understand your monthly expenses with our detailed cost breakdown tool',
              },
              {
                icon: '🏦',
                title: 'Bank Advisor',
                description: 'Get personalized banking recommendations based on your needs and budget',
              },
              {
                icon: '✅',
                title: 'Relocation Checklist',
                description: 'Stay organized with a practical checklist for your first days in Abu Dhabi',
              },
            ].map((feature, idx) => (
              <div key={idx} className="card">
                <div className="card-body">
                  <div className="text-4xl mb-3">{feature.icon}</div>
                  <h3 className="card-title">{feature.title}</h3>
                  <p className="card-text text-sm">{feature.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section id="how-it-works" className="section bg-slate-50">
        <div className="container-custom">
          <div className="section-title text-center">
            <h2 className="mb-4">How FirstDay Works</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Get started in three simple steps
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                step: '1',
                title: 'Input Your Details',
                description: 'Tell us about your lifestyle, budget, work location, and preferences',
              },
              {
                step: '2',
                title: 'Get Personalized Recommendations',
                description: 'Receive tailored suggestions for neighborhoods, banks, and costs',
              },
              {
                step: '3',
                title: 'Start Your Journey',
                description: 'Use our checklist and guides to make your move as smooth as possible',
              },
            ].map((item, idx) => (
              <div key={idx} className="relative">
                <div className="flex flex-col items-center">
                  <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold text-lg mb-4">
                    {item.step}
                  </div>
                  <h3 className="text-xl font-semibold text-center mb-2">{item.title}</h3>
                  <p className="text-slate-600 text-center text-sm">{item.description}</p>
                </div>
                {idx < 2 && (
                  <div className="hidden md:block absolute top-6 left-1/2 w-8 h-1 bg-gradient-to-r from-transparent to-blue-200 translate-x-6 -rotate-90" />
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="section">
        <div className="container-custom">
          <div className="section-title text-center">
            <h2 className="mb-4">Our Services</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Data-driven insights to help you make informed decisions
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-12">
            {[
              {
                title: 'Neighborhood Recommendations',
                description:
                  'Discover neighborhoods that align with your lifestyle and budget. Our algorithm considers affordability, commute time, amenities, and walkability to find your perfect match.',
                features: [
                  'Affordability scoring',
                  'Commute analysis',
                  'Lifestyle matching',
                  'Walkability ratings',
                ],
              },
              {
                title: 'Cost Estimation',
                description:
                  'Plan your budget with confidence. We provide detailed breakdowns of housing, utilities, dining, and miscellaneous expenses based on your preferred lifestyle.',
                features: [
                  'Housing costs',
                  'Utility estimates',
                  'Dining budgets',
                  'Transportation costs',
                ],
              },
            ].map((service, idx) => (
              <div key={idx} className="card">
                <div className="card-body">
                  <h3 className="card-title text-2xl mb-4">{service.title}</h3>
                  <p className="card-text mb-6">{service.description}</p>
                  <ul className="space-y-2">
                    {service.features.map((feature, featureIdx) => (
                      <li key={featureIdx} className="flex items-center gap-2">
                        <span className="text-green-500">✓</span>
                        <span className="text-slate-600">{feature}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Trust Section */}
      <section className="section bg-slate-50">
        <div className="container-custom text-center">
          <h2 className="mb-12">Trusted by Your Community</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-8">
            {[
              { label: 'Cities', value: '1' },
              { label: 'Neighborhoods', value: '8' },
              { label: 'Banks', value: '4' },
              { label: 'Checklist Items', value: '12' },
              { label: 'Daily Users', value: '1000+' },
              { label: 'Relocations Aided', value: '500+' },
            ].map((stat, idx) => (
              <div key={idx}>
                <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                  {stat.value}
                </div>
                <div className="text-slate-600 text-sm">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
        <div className="container-custom text-center">
          <h2 className="text-white mb-6">Ready to Start Your Journey?</h2>
          <p className="text-xl mb-8 text-blue-100 max-w-2xl mx-auto">
            Join thousands of expats who have successfully relocated to Abu Dhabi with FirstDay UAE.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-white text-blue-600 hover:bg-slate-100 font-semibold px-8 py-3 rounded-lg transition-all">
              Explore Now
            </button>
            <button className="border-2 border-white text-white hover:bg-white hover:text-blue-600 font-semibold px-8 py-3 rounded-lg transition-all">
              Learn More
            </button>
          </div>
        </div>
      </section>
    </>
  );
}
