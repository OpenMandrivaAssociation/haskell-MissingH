%global debug_package %{nil}
#% define _cabal_setup Setup.lhs
%define module MissingH
Name:           haskell-%{module}
Version:        1.2.0.0
Release:        2
Summary:        Large utility library
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(HUnit), haskell(hslogger), haskell(network)
buildrequires:  haskell(parsec), haskell(random), haskell(regex-compat)
Requires:       ghc
requires:       haskell(HUnit)
requires:       haskell(hslogger)
requires:       haskell(network)
requires:       haskell(random)
requires:       haskell(regex-compat)

%description
MissingH is a library of all sorts of utility functions for
Haskell programmers.  It is written in pure Haskell and thus should
be extremely portable and easy to use.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build


%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



