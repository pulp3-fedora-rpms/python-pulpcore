# Created by pyp2rpm-3.3.2
%global pypi_name pulpcore

Name:           python-%{pypi_name}
Version:        3.0.0b21
Release:        1%{?dist}
Summary:        Pulp Django Application and Related Modules

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(coreapi)
BuildRequires:  python3dist(django) >= 2.0
BuildRequires:  python3dist(django-filter)
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(djangorestframework-queryfields)
BuildRequires:  python3dist(drf-nested-routers)
BuildRequires:  python3dist(drf-yasg)
BuildRequires:  python3dist(dynaconf) >= 1.0.4
BuildRequires:  python3dist(gunicorn)
BuildRequires:  python3dist(psycopg2-binary)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(rq) >= 0.12.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(whitenoise)

%description
[![Build Status]( [![PyPI]( [![codecov]( [![Code Quality: Python]( [![Total
Alerts]( Organize, and Distribute Software**

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coreapi)
Requires:       python3dist(django) >= 2.0
Requires:       python3dist(django-filter)
Requires:       python3dist(djangorestframework)
Requires:       python3dist(djangorestframework-queryfields)
Requires:       python3dist(drf-nested-routers)
Requires:       python3dist(drf-yasg)
Requires:       python3dist(dynaconf) >= 1.0.4
Requires:       python3dist(gunicorn)
Requires:       python3dist(psycopg2-binary)
Requires:       python3dist(pyyaml)
Requires:       python3dist(rq) >= 0.12.0
Requires:       python3dist(setuptools)
Requires:       python3dist(whitenoise)
%description -n python3-%{pypi_name}
[![Build Status]( [![PyPI]( [![codecov]( [![Code Quality: Python]( [![Total
Alerts]( Organize, and Distribute Software**


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pulp-content
%{_bindir}/pulp-manager
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Feb 26 2019 Mike DePaulo <mikedep333@gmail.com> - 3.0.0b21-1
- Initial package.
