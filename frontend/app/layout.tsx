import type { Metadata } from 'next';
import { Navbar } from '@/components/navbar';
import { Footer } from '@/components/footer';
import './globals.css';

export const metadata: Metadata = {
  title: 'FirstDay UAE - Relocation Intelligence for Abu Dhabi',
  description: 'Your comprehensive relocation platform for moving to Abu Dhabi. Get neighborhood recommendations, cost estimates, bank advice, and a relocation checklist.',
  keywords: ['Abu Dhabi', 'relocation', 'expat', 'moving', 'UAE', 'neighborhood', 'cost calculator'],
  authors: [{ name: 'FirstDay UAE' }],
  openGraph: {
    title: 'FirstDay UAE - Relocation Intelligence',
    description: 'Your comprehensive relocation platform for moving to Abu Dhabi.',
    type: 'website',
    locale: 'en_AE',
    url: 'https://firstday-uae.com',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'FirstDay UAE',
    description: 'Relocation intelligence for Abu Dhabi',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen bg-slate-50">
        <Navbar />
        <main className="flex-1">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
