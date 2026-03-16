import Link from 'next/link';

export function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-white border-t border-slate-200">
      <div className="container-custom py-12 md:py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 mb-8">
          {/* Brand section */}
          <div className="max-w-md">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-lg flex items-center justify-center flex-shrink-0">
                <span className="text-white font-bold text-lg">FD</span>
              </div>
              <h3 className="font-bold text-lg text-slate-900">FirstDay UAE</h3>
            </div>
            <p className="text-sm text-slate-600 leading-relaxed mb-6">
              Free, open-source tools to help newcomers settle into Abu Dhabi. Built by people who've moved here.
            </p>
            <a
              href="https://github.com/rdsouza/firstday-uae"
              className="inline-flex items-center gap-2 text-slate-600 hover:text-blue-600 font-medium transition-colors"
            >
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 0C4.477 0 0 4.484 0 10.017c0 4.425 2.865 8.18 6.839 9.49.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.603-3.369-1.343-3.369-1.343-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.544 2.914 1.186.092-.923.35-1.546.636-1.903-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0110 4.817a9.573 9.573 0 012.503.337c1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48 3.97-1.31 6.833-5.066 6.833-9.487C20 4.485 15.523 0 10 0z" clipRule="evenodd" />
              </svg>
              View on GitHub
            </a>
          </div>

          {/* Quick links */}
          <div>
            <h4 className="font-semibold text-slate-900 mb-6">Tools</h4>
            <ul className="space-y-3 text-sm">
              <li>
                <Link href="#features" className="text-slate-600 hover:text-blue-600 transition-colors">
                  Neighborhood Finder
                </Link>
              </li>
              <li>
                <Link href="#features" className="text-slate-600 hover:text-blue-600 transition-colors">
                  Cost Calculator
                </Link>
              </li>
              <li>
                <Link href="#features" className="text-slate-600 hover:text-blue-600 transition-colors">
                  Bank Advisor
                </Link>
              </li>
              <li>
                <Link href="#features" className="text-slate-600 hover:text-blue-600 transition-colors">
                  Moving Checklist
                </Link>
              </li>
            </ul>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-slate-200 my-8 pt-8">
          <p className="text-sm text-slate-600 text-center">
            © {currentYear} FirstDay UAE • <a href="https://github.com/rdsouza/firstday-uae" className="hover:text-blue-600 transition-colors">Open source</a> • Free for everyone
          </p>
        </div>
      </div>
    </footer>
  );
}
