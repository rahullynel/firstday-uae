/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
  },
  
  // Image optimization
  images: {
    unoptimized: true,
    domains: [],
  },
  
  // Headers and redirects
  headers: async () => [
    {
      source: "/api/:path*",
      headers: [
        {
          key: "Cache-Control",
          value: "no-cache",
        },
      ],
    },
  ],
};

module.exports = nextConfig;
