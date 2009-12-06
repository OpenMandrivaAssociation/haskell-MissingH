%define module missingh

Name: haskell-%{module}
Version: 0.18.1
Release: %mkrel 6
Summary: Large utility library
Group: Development/Other
License: GPL
Url: http://software.complete.org/missingh
Source: http://software.complete.org/missingh/static/download_area/0.18.1/missingh_%{version}.tar.bz2
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros
BuildRequires: haskell-filepath
BuildRequires: haskell-hslogger

%description
Large utility library

%prep
%setup -q -n %{module}

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
%doc dist/doc/html
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot


