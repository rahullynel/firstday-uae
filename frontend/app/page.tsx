'use client';

import Link from 'next/link';
import Image from 'next/image';

  return (
    <>
      {/* Hero Section */}
      <section className="section bg-gradient-to-br from-blue-50 via-white to-cyan-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <div className="animate-fade-in pt-8">
              <h1 className="mb-8">
                Your Relocation Journey Starts Here
              </h1>
              <p className="text-lg md:text-xl text-slate-600 mb-10 leading-relaxed max-w-lg">
                Find the perfect neighborhood, understand your costs, choose the best bank, and settle into Abu Dhabi with confidence.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 mb-8">
                <button className="btn-primary">
                  Explore Now
                </button>
                <button className="btn-secondary">
                  Learn More
                </button>
              </div>
              <div className="flex gap-6 text-sm text-slate-500">
                <div>✓ Free</div>
                <div>✓ Data-driven</div>
                <div>✓ Trusted</div>
              </div>
            </div>
            <div className="hidden lg:flex items-center justify-center">
              <div className="relative w-full max-w-sm aspect-square bg-gradient-to-br from-blue-400 to-cyan-400 rounded-3xl shadow-2xl overflow-hidden">
                <div className="absolute inset-0 bg-opacity-10 bg-white flex items-center justify-center">
                  <svg className="w-40 h-40 text-white opacity-40" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10.5 1.5H5.75A2.25 2.25 0 003.5 3.75v12.5A2.25 2.25 0 005.75 18.5h8.5a2.25 2.25 0 002.25-2.25V6.5M10.5 1.5v5h5M10.5 1.5H9.25A1.25 1.25 0 008 2.75v3.5A1.25 1.25 0 009.25 7.5h1.25" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="section bg-white">
        <div className="container-custom">
          <div className="section-title text-center">
            <h2 className="mb-6">Everything You Need</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Comprehensive tools for expats relocating to Abu Dhabi
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {[
              {
                icon: '🏘️',
                title: 'Neighborhoods',
                description: 'Find communities that match your lifestyle and budget',
              },
              {
                icon: '💰',
                title: 'Cost Estimator',
                description: 'Understand your monthly living expenses',
              },
              {
                icon: '🏦',
                title: 'Bank Advisor',
                description: 'Personalized banking recommendations',
              },
              {
                icon: '✅',
                title: 'Checklist',
                description: 'Your relocation roadmap to success',
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
            <h2 className="mb-6">How It Works</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Three simple steps to your perfect move
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-12">
            {[
              {
                step: '1',
                title: 'Tell Us Your Details',
                description: 'Share your lifestyle, budget, and work location',
              },
              {
                step: '2',
                title: 'Get Recommendations',
                description: 'Receive personalized suggestions for your needs',
              },
              {
                step: '3',
                title: 'Start Moving',
                description: 'Use our tools and checklist every step of the way',
              },
            ].map((item, idx) => (
              <div key={idx} className="relative">
                <div className="flex flex-col items-center">
                  <div className="w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-cyan-500 text-white flex items-center justify-center font-bold text-2xl mb-6">
                    {item.step}
                  </div>
                  <h3 className="text-2xl font-semibold text-center mb-3">{item.title}</h3>
                  <p className="text-slate-600 text-center">{item.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="section bg-white">
        <div className="container-custom">
          <div className="section-title text-center">
            <h2 className="mb-6">Our Key Features</h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Data-driven tools to support your relocation
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-16">
            {[
              {
                title: 'Neighborhood Recommendations',
                description:
                  'Discover neighborhoods that align with your lifestyle and budget. Our algorithm scores for affordability, commute, amenities, and walkability.',
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
                  'Plan your budget confidently with detailed expense breakdowns for housing, utilities, dining, and transport.',
                features: [
                  'Housing costs',
                  'Utility estimates',
                  'Dining budgets',
                  'Transportation',
                ],
              },
            ].map((service, idx) => (
              <div key={idx} className="card">
                <div className="card-body">
                  <h3 className="card-title mb-4">{service.title}</h3>
                  <p className="card-text mb-8">{service.description}</p>
                  <ul className="space-y-3">
                    {service.features.map((feature, featureIdx) => (
                      <li key={featureIdx} className="flex items-center gap-3">
                        <span className="text-green-500 text-lg">✓</span>
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
      <section className="section bg-white">
        <div className="container-custom text-center">
          <h2 className="mb-16">Trusted by Relocators</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-12 md:gap-16">
            {[
              { label: 'City', value: '1' },
              { label: 'Neighborhoods', value: '8' },
              { label: 'Banks', value: '4' },
              { label: 'Checklist Items', value: '12' },
              { label: 'Users', value: '1000+' },
              { label: 'Relocations', value: '500+' },
            ].map((stat, idx) => (
              <div key={idx}>
                <div className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent mb-3">
                  {stat.value}
                </div>
                <div className="text-slate-600">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
        <div className="container-custom text-center">
          <h2 className="text-white mb-6">Ready to Begin?</h2>
          <p className="text-lg text-blue-100 max-w-2xl mx-auto mb-10">
            Join thousands already using FirstDay UAE for their relocation.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-white text-blue-600 hover:bg-slate-100 font-semibold px-8 py-3 rounded-lg transition-all">
              Get Started
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
