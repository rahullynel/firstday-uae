'use client';

import Link from 'next/link';
import { useState } from 'react';

export function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm">
      <div className="container-custom">
        <div className="flex items-center justify-between h-16 md:h-20">
          {/* Logo and brand */}
          <Link href="/" className="flex items-center gap-2">
            <div className="w-8 h-8 md:w-10 md:h-10 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-lg flex items-center justify-center flex-shrink-0">
              <span className="text-white font-bold text-lg md:text-xl">FD</span>
            </div>
            <span className="hidden sm:inline font-bold text-lg md:text-xl text-slate-900">
              FirstDay UAE
            </span>
          </Link>

          {/* Desktop navigation */}
          <div className="hidden md:flex items-center gap-8 flex-1 ml-8">
            <Link href="#features" className="text-slate-600 hover:text-blue-600 font-medium transition-colors">
              Features
            </Link>
            <Link href="#how-it-works" className="text-slate-600 hover:text-blue-600 font-medium transition-colors">
              How it Works
            </Link>
            <a href="https://github.com/rdsouza/firstday-uae" className="text-slate-600 hover:text-blue-600 font-medium transition-colors">
              GitHub
            </a>
          </div>

          {/* CTA Buttons - Desktop */}
          <div className="hidden md:flex items-center gap-3">
            <button className="btn-secondary">
              Get Started
            </button>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden p-2 rounded-lg hover:bg-slate-100 transition-colors"
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
          >
            <svg
              className="w-6 h-6 text-slate-900"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              {isOpen ? (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M6 18L18 6M6 6l12 12"
                />
              ) : (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 6h16M4 12h16M4 18h16"
                />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile navigation menu */}
        {isOpen && (
          <div className="md:hidden border-t border-slate-200 bg-white">
            <div className="px-4 py-4 space-y-3">
              <Link
                href="#features"
                className="block px-3 py-2 rounded-lg hover:bg-slate-100 text-slate-600 font-medium transition-colors"
                onClick={() => setIsOpen(false)}
              >
                Features
              </Link>
              <Link
                href="#how-it-works"
                className="block px-3 py-2 rounded-lg hover:bg-slate-100 text-slate-600 font-medium transition-colors"
                onClick={() => setIsOpen(false)}
              >
                How it Works
              </Link>
              <a
                href="https://github.com/rdsouza/firstday-uae"
                className="block px-3 py-2 rounded-lg hover:bg-slate-100 text-slate-600 font-medium transition-colors"
                onClick={() => setIsOpen(false)}
              >
                GitHub
              </a>
              <div className="pt-2 border-t border-slate-200">
                <button className="w-full btn-secondary text-sm">
                  Get Started
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}
