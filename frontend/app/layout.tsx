import type { Metadata } from 'next';
import { Navbar } from '@/components/navbar';
import { Footer } from '@/components/footer';
import './globals.css';

export const metadata: Metadata = {
  title: 'FirstDay UAE - Free Relocation Tools for Abu Dhabi',
  description: 'Free, open-source tools to help you relocate to Abu Dhabi. Find neighborhoods, calculate costs, get bank recommendations, and plan your move.',
  keywords: ['Abu Dhabi', 'UAE', 'relocation', 'expat', 'moving', 'free tools', 'open source'],
  authors: [{ name: 'FirstDay UAE' }],
  openGraph: {
    title: 'FirstDay UAE - Free Relocation Tools',
    description: 'Free, open-source tools to help you relocate to Abu Dhabi.',
    type: 'website',
    locale: 'en_AE',
    url: 'https://firstday-uae.com',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'FirstDay UAE',
    description: 'Free tools for relocating to Abu Dhabi',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen bg-white">
        <Navbar />
        <main className="flex-1">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
