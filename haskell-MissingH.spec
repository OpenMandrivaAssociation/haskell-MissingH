%define module MissingH

Name: haskell-%{module}
Version: 1.1.0.1
Release: %mkrel 1
Summary: Large utility library
Group: Development/Other
License: GPL
Url: http://software.complete.org/missingh
Source: http://software.complete.org/missingh/static/download_area/0.18.1/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros
BuildRequires: haskell(filepath)
BuildRequires: haskell(hslogger)
BuildRequires: haskell(testpack)
Obsoletes: haskell-missingh < 1.1.0.1

%description
MissingH is a library of all sorts of utility functions for Haskell
programmers. It is written in pure Haskell and thus should be extremely
portable and easy to use.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_libdir/*
%_docdir/%{module}-%{version}
%_cabal_rpm_files

%clean
rm -fr %buildroot
