%{?scl:%scl_package nodejs-%{srcname}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global srcname is-property

Name:           %{?scl_prefix}nodejs-%{srcname}
Version:        1.0.2
Release:        3%{?dist}
Summary:        Tests if a json property can be safely accessed using the .syntax

License:        MIT
URL:            https://github.com/mikolalysenko/is-property
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/mikolalysenko/is-property/master/test/test.js

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  %{?scl_prefix}npm(tap)
#BuildRequires:  %{?scl_prefix}npm(tape)

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules
mkdir test
cp -p %{SOURCE1} ./test

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json is-property.js \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#tap test/*.js

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-3
- Built for RHSCL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.2-1
- Initial packaging
