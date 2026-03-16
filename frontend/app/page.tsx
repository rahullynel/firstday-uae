'use client';

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="section bg-gradient-to-br from-blue-50 via-white to-cyan-50">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto text-center animate-fade-in">
            <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-slate-900 mb-6">
              Your first week in the UAE, made simpler.
            </h1>
            <p className="text-lg md:text-xl text-slate-600 mb-12 leading-relaxed max-w-2xl mx-auto">
              Free, open-source tools to help you find neighborhoods, estimate costs, understand banking options, and plan your relocation with confidence.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
              <button className="btn-primary">
                Explore Tools
              </button>
              <a
                href="https://github.com/rdsouza/firstday-uae"
                className="btn-secondary"
              >
                View on GitHub
              </a>
            </div>
            <div className="flex flex-wrap gap-8 justify-center text-sm text-slate-600 max-w-xl mx-auto">
              <div className="flex items-center gap-2">
                <span className="text-green-600 font-bold">✓</span>
                <span>100% Free</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-green-600 font-bold">✓</span>
                <span>Open Source</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-green-600 font-bold">✓</span>
                <span>Built by Relocators</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="section bg-white">
        <div className="container-custom">
          <div className="text-center mb-16 md:mb-20">
            <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
              Four Essential Tools
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Everything you need to settle into Abu Dhabi confidently
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: '🏘️',
                title: 'Neighborhood Finder',
                description: 'Discover neighborhoods that match your lifestyle and budget. Compare affordability, commute times, and walkability.',
              },
              {
                icon: '💰',
                title: 'Cost Calculator',
                description: 'Calculate your monthly expenses based on lifestyle choices. Understand your budget before you move.',
              },
              {
                icon: '🏦',
                title: 'Bank Advisor',
                description: 'Get personalized bank recommendations. Compare accounts, salaries requirements, and features.',
              },
              {
                icon: '✅',
                title: 'Moving Checklist',
                description: 'Stay organized with a comprehensive checklist. Actions grouped by timeline from day 1 to settling in.',
              },
            ].map((feature, idx) => (
              <div key={idx} className="card">
                <div className="card-body">
                  <div className="text-5xl mb-4">{feature.icon}</div>
                  <h3 className="text-xl font-semibold text-slate-900 mb-3">
                    {feature.title}
                  </h3>
                  <p className="text-slate-600 leading-relaxed">
                    {feature.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section id="how-it-works" className="section bg-slate-50">
        <div className="container-custom">
          <div className="text-center mb-16 md:mb-20">
            <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
              How It Works
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              Get started in three simple steps
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-12">
            {[
              {
                step: '1',
                title: 'Choose Your Tool',
                description: 'Select the tool that matches your immediate need—neighborhoods, budgets, banking, or moving checklist.',
              },
              {
                step: '2',
                title: 'Input Your Preferences',
                description: 'Share relevant details like lifestyle, salary range, or timeline. All info stays on your device.',
              },
              {
                step: '3',
                title: 'Get Your Results',
                description: 'Receive personalized recommendations, calculations, and plans tailored to your situation.',
              },
            ].map((item, idx) => (
              <div key={idx} className="text-center">
                <div className="flex justify-center mb-6">
                  <div className="w-16 h-16 rounded-full bg-gradient-to-br from-blue-500 to-cyan-500 text-white flex items-center justify-center font-bold text-2xl">
                    {item.step}
                  </div>
                </div>
                <h3 className="text-2xl font-semibold text-slate-900 mb-3">
                  {item.title}
                </h3>
                <p className="text-slate-600 leading-relaxed">
                  {item.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Section */}
      <section className="section bg-white">
        <div className="container-custom">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-12">
              <h2 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
                Why Choose FirstDay UAE?
              </h2>
            </div>
            <div className="grid md:grid-cols-2 gap-8">
              {[
                {
                  title: 'Built for Relocators',
                  description: 'Created by people who moved to Abu Dhabi. We understand the challenges and information you need.',
                },
                {
                  title: 'No Hidden Costs',
                  description: 'Everything is free. No premium features, no paywalls, no email capture. Just helpful tools.',
                },
                {
                  title: 'Community-Driven',
                  description: 'Open source and transparent. Contribute improvements, report issues, or customize for your needs.',
                },
                {
                  title: 'Privacy First',
                  description: 'Your data never leaves your device. All calculations happen locally. Complete transparency.',
                },
              ].map((item, idx) => (
                <div key={idx} className="card">
                  <div className="card-body">
                    <h3 className="text-xl font-semibold text-slate-900 mb-3">
                      {item.title}
                    </h3>
                    <p className="text-slate-600 leading-relaxed">
                      {item.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
        <div className="container-custom text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            Ready for Your Move?
          </h2>
          <p className="text-lg text-blue-100 max-w-2xl mx-auto mb-10">
            Start using our free tools today. No signup. No credit card. Just real help for your relocation.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-white text-blue-600 hover:bg-slate-100 font-semibold px-8 py-3 rounded-lg transition-all">
              Explore All Tools
            </button>
          </div>
        </div>
      </section>
    </>
  );
}
