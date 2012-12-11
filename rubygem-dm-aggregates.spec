# Generated from dm-aggregates-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	dm-aggregates

Summary:	DataMapper plugin providing support for aggregates on collections
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-aggregates
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
DataMapper plugin providing support for aggregates on collections

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/core_ext/
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/core_ext/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/adapters/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 767129
- imported package rubygem-dm-aggregates

